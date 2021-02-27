from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import View

from .models import *


class BaseView(View):

    def get(self, request, *args, **kwargs):
        news = LatestNews.objects.get_news_for_main_page('news')
        context = {
            'news': news,
        }
        return render(request, 'base.html', context)