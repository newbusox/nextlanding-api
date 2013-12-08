from rest_framework.response import Response
from rest_framework.views import APIView
from scrapy_test.apps.domain.search.services import emailer_sender_service


class EmailerSenderView(APIView):
  """
  API endpoint that allows sending emails for a search.
  """

  def get(self, request, *args, **kwargs):
    pk = kwargs['pk']
    emailer_sender_model = emailer_sender_service.get_search_emailer_sender(pk)

    search_data = {
      'location': emailer_sender_model.specified_location,
      'search_description': emailer_sender_model.description,
      'subject': emailer_sender_model.subject,
      'body': emailer_sender_model.body,
      'from_name': emailer_sender_model.from_name,
    }

    return Response(search_data)

  def post(self, request, *args, **kwargs):
    pk = kwargs['pk']

    emailer_sender_model = emailer_sender_service.get_search_emailer_sender(pk)

    from_name, subject, body = request.DATA['from_name'], request.DATA['subject'], request.DATA['body']

    #this will call save internally
    emailer_sender_service.send_search_email(emailer_sender_model, from_name, subject, body)

    return Response()
