from rest_framework import serializers

class CrawlerSerializer(serializers.Serializer):
  urls = serializers.ListField(
    required=True,
    child=serializers.URLField(required=True)
  )
  word = serializers.CharField(required=True)