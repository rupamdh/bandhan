# Generated by Django 5.0.7 on 2024-07-22 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='winners/')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Winners',
            },
        ),
    ]
