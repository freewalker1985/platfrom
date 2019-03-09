from django.db import models

SYSTEM_LIST = (
    ('redhat', 'redhat'),
    ('opensuse', 'opensuse'),
    ('ubuntu', 'ubuntu'),
    ('centos', 'centos'),
    ('windows', 'windows'),
    ('other', 'other'),
)

STATUS = (
    ('produce', 'produce'),
    ('test', 'test'),
    ('other', 'other'),
)


class Project(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class ServerDetail(models.Model):
    ip = models.CharField(max_length=20, unique=True)
    system = models.CharField(choices=SYSTEM_LIST, default='centos', max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    cpuinfo = models.CharField(max_length=50)
    memory = models.IntegerField()
    status = models.CharField(choices=STATUS, default='other', max_length=50)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.ip
