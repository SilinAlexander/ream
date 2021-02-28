from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BaseView.as_view(), name='base'),
    path('article/<slug>/', views.NewsDetail.as_view(), name='news_detail')

    ]