# Generated by Django 4.1.7 on 2023-06-10 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0002_payment_cleaning_id_alter_payment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='card',
            field=models.CharField(default=False, max_length=30),
        ),
    ]
