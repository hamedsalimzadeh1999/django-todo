# Generated by Django 3.0.8 on 2020-08-01 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='Date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='DueDate',
            field=models.DateTimeField(null=True),
        ),
    ]
