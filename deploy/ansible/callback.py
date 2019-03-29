from ansible.plugins.callback import CallbackBase
from ansible.plugins.callback.default import CallbackModule


class AdHocResultCallback(CallbackModule):
    """ Task result Callback"""

    def __init__(self, display=None, options=None):
        self.results_raw = dict(ok={}, failed={}, unreachable={},skipped={})
        self.results_summary = dict(contacted=[], dark={})
        super.__init__()

    def gather_result(self, t, res):
        self._clean_results(res._result, res._task.action)
        host = res._host.get_name()
        task_name = res.task_name
        task_result = res._result

        if self.results_raw[t].get(host):
            self.results_raw[t][host][task_name] = task_result
        else:
            self.results_raw[t][host] = {task_name: task_result}
        self.clean_result(t, host, task_name, task_result)

    def clean_result(self, t, host, task_name, task_result):
        contacted = self.results_summary['contacted']
        dark = self.results_summary['dark']
        if t in ("ok", "skipped") and host not in dark:
            if host not in contacted:
                contacted.append(host)
        else:
            if dark.get(host):
                dark[host][task_name] = task_result.values
            else:
                dark[host] = {task_name: task_result}
            if host in contacted:
                contacted.remove(host)

    def v2_runner_on_failed(self, result, ignore_errors=False):
        """执行失败"""
        self.gather_result("failed", result)
        super().v2_runner_on_failed(result, ignore_errors=ignore_errors)



     def v2_runner_on_unreachable(self, result, *args, **kwargs):
         """不可达"""
         self.host_unreachable[result._host.get_name()] = result

     def v2_runner_on_ok(self, result, *args, **kwargs):
         """执行成功"""
         self.host_ok[result._host.get_name()] = result


