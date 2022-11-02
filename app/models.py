from django.db import models


# Create your models here.
class UserInfo(models.Model):
    user_name = models.CharField(verbose_name='ユーザ名', max_length=32)
    birth_day = models.DateField(verbose_name='生年月日')
    age = models.PositiveIntegerField(verbose_name='年齢', null=True, unique=False)
    created_at = models.DateField(verbose_name='作成日時', auto_now_add=True)
