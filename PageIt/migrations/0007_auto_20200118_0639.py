# Generated by Django 3.0.2 on 2020-01-18 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PageIt', '0006_auto_20200118_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
    ]