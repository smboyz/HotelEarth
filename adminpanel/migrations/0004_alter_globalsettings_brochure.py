# Generated by Django 4.1.7 on 2023-08-02 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0003_globalsettings_brochure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalsettings',
            name='brochure',
            field=models.FileField(default=None, null=True, upload_to='brochurefile/'),
        ),
    ]
