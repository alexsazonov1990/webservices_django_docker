# Generated by Django 3.1.2 on 2021-02-10 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationForDevelopmentCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.TextField(verbose_name='Что разрабатываем\\дорабатываем')),
                ('purpose', models.TextField(verbose_name='Что должно быть в готовом варианте')),
                ('why_necessary', models.TextField(verbose_name='Зачем необходима доработка\\разработка')),
                ('why_use_it', models.TextField(verbose_name='Кто будет использовать')),
                ('where_used', models.TextField(verbose_name='Где будут использовать')),
                ('full_name_customer', models.CharField(max_length=200, verbose_name='Фио заказчика')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Заявка на разработку',
                'verbose_name_plural': 'Заявки на разработку',
            },
        ),
    ]
