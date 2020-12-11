# Generated by Django 3.1.3 on 2020-12-04 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20201204_0957'),
    ]

    operations = [
        migrations.CreateModel(
            name='PowerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=15, verbose_name='用户ID')),
                ('power', models.CharField(max_length=30, verbose_name='权限')),
                ('team', models.IntegerField(default=60, verbose_name='组别')),
            ],
            options={
                'db_table': 'power',
            },
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=10, verbose_name='用户名')),
                ('password', models.CharField(max_length=10, verbose_name='密码')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='UserInformationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=15, verbose_name='用户id')),
                ('user_name', models.CharField(max_length=30, verbose_name='用户姓名')),
                ('user_team', models.CharField(max_length=20, verbose_name='用户团队')),
            ],
            options={
                'db_table': 'userinformation',
            },
        ),
    ]
