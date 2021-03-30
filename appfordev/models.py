# Create your models here.

from django.db import models


class ApplicationForDevelopmentCard(models.Model):
    topic = models.TextField(verbose_name='Что разрабатываем\дорабатываем')
    purpose = models.TextField(verbose_name='Что должно получиться в готовом варианте.Пример: форма которую '
                                            'необходимо заполнять,кнопка и тд')
    why_necessary = models.TextField(verbose_name='Опишите подробно, какую проблему решает данная доработка, к чему '
                                                  'мы хотим прийти в итоге')

    why_use_it = models.TextField(verbose_name='Опишите кто будет '
                                               'использовать: врачи,медсестры,'
                                               'заведующие отделениями, прочие '
                                               'подразделения и тд')
    where_used = models.TextField(verbose_name='Где будут использовать: В базе приемы, в базе расписания, прочее')
    full_name_customer = models.CharField(max_length=200, verbose_name='Фио заказчика')
    email = models.EmailField(verbose_name='Email')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.topic


# Загрузка файлов\скриншотов и тд.
class MyModel(models.Model):
    upload = models.FileField(blank=True, null=True, verbose_name='')
