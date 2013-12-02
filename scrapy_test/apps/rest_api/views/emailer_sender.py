from rest_framework.response import Response
from rest_framework.views import APIView
from scrapy_test.aggregates.search.services import search_service
from scrapy_test.apps.domain.constants import EMAILER_SENDER_SUBJECT_TEMPLATE, \
  EMAILER_SENDER_BODY_TEMPLATE


class EmailerSenderView(APIView):
  """
  API endpoint that allows sending emails for a search.
  """

  def get(self, request, *args, **kwargs):
    pk = kwargs['pk']
    search = search_service.get_search(pk)

    search_data = {
      'id': search.pk,
      'location': search.specified_location,
      'search_description': search.description,
      'subject': EMAILER_SENDER_SUBJECT_TEMPLATE,
      'body': EMAILER_SENDER_BODY_TEMPLATE,
    }

    return Response(search_data)

  def post(self, request, *args, **kwargs):
    pk = kwargs['pk']

    search = search_service.get_search(pk)

    from_name, subject, body = request.DATA['from_name'], request.DATA['subject'], request.DATA['body']
    search.request_availability_from_contacts(from_name,subject,body)

    search_service.save_or_update(search)

    return Response()
