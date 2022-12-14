# Generated by Django 4.1.3 on 2022-11-08 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='日時')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('content', models.TextField(verbose_name='本文')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='作成日時')),
            ],
        ),
    ]
