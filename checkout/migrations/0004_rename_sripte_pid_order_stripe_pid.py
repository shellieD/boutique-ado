# Generated by Django 3.2 on 2022-07-16 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20220716_2020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='sripte_pid',
            new_name='stripe_pid',
        ),
    ]
