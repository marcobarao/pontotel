from django.db import models
from bs4 import BeautifulSoup
import requests
import re

# Create your models here.
class Crawler():
  def __init__(self, urls, word):
    self._urls = urls
    self._word = word
    self._result = {}
  
  def run(self):
    print(self._urls)
    for url in self._urls:
      page_response = requests.get(url, timeout=5).text
      page_content = BeautifulSoup(page_response, "html.parser").get_text()
      regex = r"\W" + re.escape(self._word) + r"\W+"
      result = re.findall(regex, page_content, re.IGNORECASE)
      occurencies = len(result)
      self._result[url] = (occurencies if occurencies <= 3 else occurencies - 1) 

  def result(self):
    return self._result
