# Generated by Django 2.2.1 on 2019-05-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/images/default.jpg', upload_to='media/images/'),
        ),
    ]