from rest_framework import serializers

class CrawlerSerializer(serializers.Serializer):
  urls = serializers.ListField(
    child=serializers.URLField(),
    
  )
  word = serializers.CharField()