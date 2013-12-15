from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from nextlanding_api.apps.web_scraper.services import web_scraper_tasks


class CrawlView(APIView):
  """
  API endpoint for crawls.
  """
  def post(self, request, *args, **kwargs):
    crawl_urls = request.DATA['crawl_urls']

    for crawl in crawl_urls:
      web_scraper_tasks.crawl_individual_page_task.delay(crawl)

    return Response(status=status.HTTP_201_CREATED)
