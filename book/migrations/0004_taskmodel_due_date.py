# Generated by Django 4.2.7 on 2024-03-07 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_taskmodel_priotiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='due_date',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
