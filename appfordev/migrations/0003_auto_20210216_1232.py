# Generated by Django 3.1.2 on 2021-02-16 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfordev', '0002_auto_20210212_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name=''),
        ),
    ]
