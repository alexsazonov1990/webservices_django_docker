# Generated by Django 3.1.2 on 2021-02-18 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfordev', '0004_auto_20210217_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name=''),
        ),
    ]
