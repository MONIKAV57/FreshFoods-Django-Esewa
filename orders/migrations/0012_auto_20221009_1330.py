# Generated by Django 3.2.15 on 2022-10-09 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20220730_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='payment',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('New', 'New'), ('Cancelled', 'Cancelled'), ('Accepted', 'Accepted')], default='New', max_length=10),
        ),
    ]
