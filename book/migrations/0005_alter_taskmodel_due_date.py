# Generated by Django 4.2.7 on 2024-03-07 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_taskmodel_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='due_date',
            field=models.DateField(null=True),
        ),
    ]
