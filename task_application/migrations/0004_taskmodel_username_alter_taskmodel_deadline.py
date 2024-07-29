# Generated by Django 5.0.6 on 2024-05-27 05:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_application', '0003_alter_taskmodel_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 26, 5, 45, 3, 515047)),
        ),
    ]
