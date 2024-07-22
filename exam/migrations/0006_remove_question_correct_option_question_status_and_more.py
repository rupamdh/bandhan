# Generated by Django 5.0.7 on 2024-07-22 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='correct_option',
        ),
        migrations.AddField(
            model_name='question',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans',
            field=models.TextField(editable=False),
        ),
    ]
