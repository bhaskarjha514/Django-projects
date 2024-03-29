# Generated by Django 2.2.3 on 2019-10-21 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0014_auto_20191010_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='pictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='students/memories/Albums')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Albums')),
            ],
        ),
    ]
