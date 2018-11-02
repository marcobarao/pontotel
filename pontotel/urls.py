from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view

from crawler import views


schema_view = get_swagger_view(title='Snippets API')

urlpatterns = [
    url('^$', schema_view),
    url(r'crawler', views.CrawlerAPI.as_view(), name="crawler")
]