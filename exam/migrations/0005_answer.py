# Generated by Django 5.0.7 on 2024-07-22 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_alter_question_correct_option'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('ans', models.TextField()),
            ],
        ),
    ]
