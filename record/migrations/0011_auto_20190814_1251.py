# Generated by Django 2.2.4 on 2019-08-14 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0010_auto_20190814_1250'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='article',
            name='name of constraint',
        ),
    ]
