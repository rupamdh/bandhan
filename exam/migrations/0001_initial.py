# Generated by Django 5.0.7 on 2024-07-22 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('option_1', models.CharField(max_length=200)),
                ('option_2', models.CharField(max_length=200)),
                ('option_3', models.CharField(max_length=200)),
                ('option_4', models.CharField(max_length=200)),
                ('correct_option', models.CharField(choices=[(1, models.CharField(max_length=200)), (2, models.CharField(max_length=200)), (3, models.CharField(max_length=200)), (4, models.CharField(max_length=200))], max_length=200)),
            ],
        ),
    ]
