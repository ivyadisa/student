# Generated by Django 5.0 on 2024-01-14 22:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0014_mark_grade_mark_remark'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mark',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='remark',
        ),
        migrations.AddField(
            model_name='classteacher',
            name='selection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.classsubject'),
        ),
    ]
