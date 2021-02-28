from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views.generic.base import View

from .models import *


class BaseView(View):

    def get(self, request, *args, **kwargs):
        news = LatestNews.objects.get_news_for_main_page('news')
        contacts = Contacts.objects.all()
        context = {
            'news': news,
            'contacts': contacts,
        }
        return render(request, 'base.html', context)


class NewsDetail(DetailView):

    model = News
    slug_url_kwarg = 'slug'
    template_name = 'main/news_detail.html'