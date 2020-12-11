# Generated by Django 3.1.3 on 2020-12-04 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_log_move_ip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log_move',
            old_name='title',
            new_name='log_name',
        ),
        migrations.RenameField(
            model_name='log_move',
            old_name='url',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='log_move',
            name='body',
        ),
        migrations.AddField(
            model_name='log_move',
            name='password',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='log_move',
            name='ports',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]