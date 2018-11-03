from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

from crawler import views


schema_view = get_swagger_view(title='Snippets API')

urlpatterns = [
    path('', schema_view),
    path('crawler', views.CrawlerAPI.as_view(), name="crawler")
]