# Generated by Django 4.0.6 on 2022-07-18 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0002_bill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paycheck',
            old_name='paycheckAmmount',
            new_name='ammount',
        ),
        migrations.RenameField(
            model_name='paycheck',
            old_name='paycheckDate',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='paycheck',
            old_name='paycheckName',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='bill',
            name='dueDate',
            field=models.IntegerField(),
        ),
    ]
