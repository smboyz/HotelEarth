# Generated by Django 4.1.7 on 2023-08-01 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.CharField(max_length=10)),
                ('check_out', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('subject', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='gallery/')),
            ],
        ),
        migrations.CreateModel(
            name='GlobalSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SiteName', models.CharField(max_length=100)),
                ('SiteContact', models.CharField(max_length=50)),
                ('SiteEmail', models.EmailField(max_length=254)),
                ('SiteAddress', models.CharField(max_length=500)),
                ('logo', models.ImageField(default=None, max_length=200, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel_Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total', models.IntegerField(null=True)),
                ('icon', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('star', models.IntegerField(null=True)),
                ('feedback', models.CharField(max_length=10000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='rooms/')),
                ('description', models.TextField(null=True)),
                ('n_bed', models.IntegerField()),
                ('n_people', models.IntegerField()),
                ('room_size', models.IntegerField()),
                ('Ac_NonAc', models.CharField(max_length=50)),
                ('price_single', models.IntegerField()),
                ('price_double', models.IntegerField()),
                ('extra_bed_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('caption', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='slider/')),
            ],
        ),
        migrations.CreateModel(
            name='Navigation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('caption', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Publish', 'Publish'), ('Draft', 'Draft')], max_length=50)),
                ('position', models.IntegerField()),
                ('page_type', models.CharField(blank=True, choices=[('Home', 'Home'), ('Service', 'Service'), ('about', 'about'), ('contact', 'contact'), ('Features', 'Features'), ('group', 'group')], max_length=50, null=True)),
                ('title', models.CharField(max_length=200)),
                ('short_desc', models.TextField(blank=True, null=True)),
                ('long_desc', models.TextField(null=True)),
                ('banner_image', models.ImageField(upload_to='about/')),
                ('meta_title', models.CharField(max_length=100, null=True)),
                ('meta_keyword', models.CharField(max_length=100, null=True)),
                ('icon_image', models.ImageField(upload_to='about/')),
                ('slider_image', models.ImageField(null=True, upload_to='about/')),
                ('image1', models.ImageField(null=True, upload_to='about/')),
                ('image2', models.ImageField(null=True, upload_to='about/')),
                ('description', models.TextField(null=True)),
                ('title1', models.CharField(max_length=200, null=True)),
                ('title2', models.CharField(max_length=200, null=True)),
                ('short_desc1', models.TextField(null=True)),
                ('short_desc2', models.TextField(null=True)),
                ('Parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='adminpanel.navigation')),
            ],
        ),
        migrations.CreateModel(
            name='Key_Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('features_type', models.CharField(choices=[('GROUP', 'GROUP'), ('PROPERTY FEATURE SERVICES', 'PROPERTY FEATURE SERVICES'), ('PROPERTY FACILITIES', 'PROPERTY FACILITIES'), ('ROOM FACILITIES', 'ROOM FACILITIES'), ('FEATURE COMPONENTS', 'FEATURE COMPONENTS')], max_length=100, null=True)),
                ('position', models.IntegerField(null=True)),
                ('icon', models.CharField(max_length=50, null=True)),
                ('Parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='adminpanel.key_feature')),
            ],
        ),
    ]
