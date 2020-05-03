# Generated by Django 3.0.5 on 2020-05-03 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20200429_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='newsletter',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='unverifiedclient',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Client'),
        ),
        migrations.AlterField(
            model_name='unverifiedclient',
            name='nonce',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='unverifiedclient',
            name='reservation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Reservation'),
        ),
    ]
