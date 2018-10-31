from django.urls import path
from .views import CrawlerList

urlpatterns = [
    path('crawler/', CrawlerList.as_view(), name='crawler-list'),
]