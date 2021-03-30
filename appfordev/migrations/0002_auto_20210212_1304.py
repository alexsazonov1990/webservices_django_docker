# Generated by Django 3.1.2 on 2021-02-12 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfordev', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='')),
            ],
        ),
        migrations.AlterModelOptions(
            name='applicationfordevelopmentcard',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AlterField(
            model_name='applicationfordevelopmentcard',
            name='purpose',
            field=models.TextField(verbose_name='Что должно получиться в готовом варианте.Пример: форма которую необходимо заполнять,кнопка и тд'),
        ),
        migrations.AlterField(
            model_name='applicationfordevelopmentcard',
            name='where_used',
            field=models.TextField(verbose_name='Где будут использовать: В базе приемы, в базе расписания, прочее'),
        ),
        migrations.AlterField(
            model_name='applicationfordevelopmentcard',
            name='why_necessary',
            field=models.TextField(verbose_name='Опишите подробно, какую проблему решает данная доработка, к чему мы хотим прийти в итоге'),
        ),
        migrations.AlterField(
            model_name='applicationfordevelopmentcard',
            name='why_use_it',
            field=models.TextField(verbose_name='Опишите кто будет использовать: врачи,медсестры,заведующие отделениями, прочие подразделения и тд'),
        ),
    ]