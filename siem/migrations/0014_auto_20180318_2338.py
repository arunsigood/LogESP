# Generated by Django 2.0.3 on 2018-03-19 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siem', '0013_auto_20180318_2329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logevent',
            old_name='referer',
            new_name='referrer',
        ),
    ]
