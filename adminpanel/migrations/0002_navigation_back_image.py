# Generated by Django 4.1.7 on 2023-08-01 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigation',
            name='back_image',
            field=models.ImageField(null=True, upload_to='about/'),
        ),
    ]
