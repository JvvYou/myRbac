# Generated by Django 4.1 on 2023-12-05 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0002_remove_userprofile_is_staff_userprofile_is_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default='', max_length=20, verbose_name='姓名'),
        ),
    ]
