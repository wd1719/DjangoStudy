from django.db import models

class Block(models.Model):
    name = models.CharField("板块名称",max_length=100)
    desc = models.CharField("板块描述", max_length=100)
    manager_name = models.CharField("管理员名字", max_length=100)
    status = models.IntegerField("状态", choices=((0,"正常"),(-1,"删除")), default=0)
    links = models.CharField("链接网址", max_length=100, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "板块"
        verbose_name_plural = "板块(s)"