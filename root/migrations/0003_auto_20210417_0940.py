# Generated by Django 3.1.3 on 2021-04-17 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_auto_20210417_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image1',
            field=models.ImageField(blank=True, upload_to='<django.db.models.fields.CharField>/'),
        ),
    ]