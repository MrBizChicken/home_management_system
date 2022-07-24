# Generated by Django 4.0.6 on 2022-07-24 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0002_chore_person_to_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='chore',
            name='money_earned',
            field=models.CharField(default='Insert Value', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chore',
            name='score',
            field=models.CharField(default='Null', max_length=200),
            preserve_default=False,
        ),
    ]
