# Generated by Django 4.1 on 2022-08-13 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_designinfo_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designinfo',
            name='design_pic',
            field=models.ImageField(upload_to='designs'),
        ),
    ]
