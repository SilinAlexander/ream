from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


class User(AbstractUser):

    username = None
    email = models.EmailField('Email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email


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




class LatestNewsManager:

    @staticmethod
    def get_news_for_main_page(*args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        news = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            news.extend(model_products)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(
                        news, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to), reverse=True
                    )
        return news

class LatestNews:

    objects = LatestNewsManager()