# Generated by Django 2.2.3 on 2019-09-15 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_auto_20190915_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='students/memories/Albums')),
                ('meetupplace', models.CharField(max_length=200)),
            ],
        ),
    ]
