from django.db import models


class Tutorial(models.Model):
    title = models.CharField(max_length=100, null=True, verbose_name='标题')
    content = models.TextField(null=True, verbose_name='内容')
    prev = models.ForeignKey('self', verbose_name='上一节', null=True, related_name='+')
    next = models.ForeignKey('self', verbose_name='下一节', null=True, related_name='+')
    level = models.IntegerField(verbose_name='等级')
    status = models.IntegerField(default=1, verbose_name='状态')
