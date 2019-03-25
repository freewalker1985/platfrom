import json
import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
import ansible.constants as C


class ResultCallback(CallbackBase):
    """重构执行结果"""

    def __init__(self, *args, **kwargs):
        super(ResultCallback, self).__init__(*args, **kwargs)
        self.host_ok = {}
        self.host_unreachable = {}
        self.host_failed = {}

    def v2_runner_on_unreachable(self, result, *args, **kwargs):
        """不可达"""
        self.host_unreachable[result._host.get_name()] = result

    def v2_runner_on_ok(self, result, *args, **kwargs):
        """执行成功"""
        self.host_ok[result._host.get_name()] = result

    def v2_runner_on_failed(self, result, *args, **kwargs):
        """执行失败"""
        self.host_failed[result._host.get_name()] = result


def run_ansible(module_name, module_args, host_list, option_dict):
    # namedtuple命名元组，使用属性名访问
    Options = namedtuple('Options',
                         ['connection', 'module_path', 'forks', 'become', 'become_method', 'private_key_file',
                          'become_user', 'remote_user',
                          'check', 'diff'])

    options = Options(connection='local', module_path=None, forks=10, become=option_dict['become'],
                      become_method='sudo', private_key_file="/root/.ssh/id_rsa",
                      become_user='root', remote_user=option_dict['remote_user'], check=False, diff=False)

    loader = DataLoader()
    passwords = dict(vault_pass='secret')

    result_callback = ResultCallback()

    # sources指定 host config file or hostname
    # 创建清单，并传递给VariableManager
    inventory = InventoryManager(loader=loader, sources=['/etc/ansible/hosts'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    host = ",".join(host_list)
    play_source = dict(
        name="Ansible Play",
        hosts=host,
        gather_facts='no',
        tasks=[
            dict(action=dict(module=module_name, args=module_args), register='shell_out'),
        ]
    )

    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

    tqm = None

    tqm = TaskQueueManager(
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        options=options,
        passwords=passwords,
        stdout_callback=result_callback,
    )

    result = tqm.run(play)

    result_raw = {'success': {}, 'failed': {}, 'unreachable': {}}

    for host, result in result_callback.host_ok.items():
        result_raw['success'][host] = result._result['stdout_lines']

    for host, result in result_callback.host_failed.items():
        result_raw['failed'][host] = result._result['stderr_lines']

    for host, result in result_callback.host_unreachable.items():
        result_raw['unreachable'][host] = result._result['msg']

    return json.dumps(result_raw, indent=4)
