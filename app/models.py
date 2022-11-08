from django.db import models


# Create your models here.
class Information(models.Model):
    date = models.DateField(verbose_name='日時')
    url = models.URLField(verbose_name='URL', null=True, blank=True, unique=False)
    content = models.TextField(verbose_name='本文')
    created_at = models.DateField(verbose_name='作成日時', auto_now_add=True)
