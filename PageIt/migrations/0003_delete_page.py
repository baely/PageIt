# Generated by Django 3.0.2 on 2020-01-18 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PageIt', '0002_remove_page_page'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Page',
        ),
    ]