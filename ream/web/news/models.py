from django.contrib.auth import get_user_model
from django.db import models
from main.models import News
# Create your models here.
User = get_user_model()


class FavouriteNews(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_news_set')
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='favorite_news_set')

    class Meta:
        verbose_name = 'Favorite news'
        unique_together = ('user', 'news')

    def __str__(self):
        return f'{self.user.email} - {self.news.title}'

