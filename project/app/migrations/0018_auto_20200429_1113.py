# Generated by Django 3.0.5 on 2020-04-29 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20200428_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='cancelled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reservation',
            name='notify_admin',
            field=models.BooleanField(default=True),
        ),
    ]