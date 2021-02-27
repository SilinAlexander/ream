from django.db import models
from django.urls import reverse_lazy


class Contacts(models.Model):

    title = models.CharField(max_length=255, verbose_name='Контакт')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('news_detail', kwargs={'slug': self.slug})


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

    def get_absolute_url(self):
        return reverse_lazy('news_detail', kwargs={'slug': self.slug})