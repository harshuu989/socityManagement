# Generated by Django 2.2.14 on 2022-06-06 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20220606_1425'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='carpenterDetails',
            new_name='carpentersDetails',
        ),
    ]