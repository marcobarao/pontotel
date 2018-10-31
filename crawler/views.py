from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from .serializers import CrawlerSerializer
from .models import Crawler
from django.http import HttpResponse

class CrawlerList(ListCreateAPIView):
  serializer_class = CrawlerSerializer

  def post(self, request):
    urls = request.data["urls"]
    word = request.data["word"]
    crawler = Crawler(urls, word)
    crawler.run()
    return Response(crawler.result())

  def get_queryset(self):
    return ''