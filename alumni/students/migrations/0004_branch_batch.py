# Generated by Django 2.2.3 on 2019-09-09 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20190909_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='batch',
            field=models.DurationField(null=True),
        ),
    ]