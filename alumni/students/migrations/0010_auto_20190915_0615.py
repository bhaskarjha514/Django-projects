# Generated by Django 2.2.3 on 2019-09-15 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_profile_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followuser',
            name='followed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_by', to='students.Profile'),
        ),
        migrations.AlterField(
            model_name='followuser',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='students.Profile'),
        ),
    ]
