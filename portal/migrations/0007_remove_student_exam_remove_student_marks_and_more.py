# Generated by Django 5.0 on 2024-01-02 10:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_remove_mark_student_student_exam_student_marks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='student',
            name='marks',
        ),
        migrations.AddField(
            model_name='mark',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.student'),
        ),
    ]
