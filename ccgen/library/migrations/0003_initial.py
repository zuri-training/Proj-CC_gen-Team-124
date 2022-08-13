# Generated by Django 4.1 on 2022-08-13 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library', '0002_delete_designinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='DesignInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design_pic', models.ImageField(upload_to='images')),
                ('likes', models.PositiveIntegerField()),
            ],
        ),
    ]
