# Generated by Django 5.0 on 2024-01-07 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_alter_mark_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='marks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='mark',
            unique_together={('student', 'subject', 'user_class', 'exam')},
        ),
    ]
