# Generated by Django 4.2.7 on 2024-03-07 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_alter_taskmodel_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='due_date',
            field=models.DateField(null=True),
        ),
    ]
