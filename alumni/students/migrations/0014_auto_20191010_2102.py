# Generated by Django 2.2.3 on 2019-10-10 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0013_albums'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='contact_detail',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='notice',
            name='venue',
            field=models.TextField(null=True),
        ),
    ]
