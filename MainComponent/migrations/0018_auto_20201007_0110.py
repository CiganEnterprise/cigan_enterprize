# Generated by Django 3.0.8 on 2020-10-06 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainComponent', '0017_auto_20201002_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='studio',
            name='manager_image',
            field=models.ImageField(default='default.jpg', upload_to='managers_image/'),
        ),
        migrations.AddField(
            model_name='studio',
            name='manager_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]