from django.http import HttpResponse
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import status, renderers

from .serializers import CrawlerSerializer
from .models import Crawler

class CrawlerAPI(CreateAPIView):
  queryset = None
  serializer_class = CrawlerSerializer

  def post(self, request, format="json"):
    serializer = CrawlerSerializer(data=request.data)
    if serializer.is_valid():
      urls = request.data["urls"]
      word = request.data["word"]
      crawler = Crawler(urls, word)
      crawler.run()
      return Response(crawler.result(), status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)