# Generated by Django 3.0 on 2019-12-18 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20191218_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image1',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='image2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
