# Generated by Django 4.0.3 on 2022-04-27 21:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_api', '0004_rename_transaction_transactions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='points',
            name='points',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]