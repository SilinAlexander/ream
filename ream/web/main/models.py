from django.db import models


class Contacts(models.Model):

    title = models.CharField(max_length=255, verbose_name='Контакт')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class News(models.Model):

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    slug = models.SlugField(unique=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title