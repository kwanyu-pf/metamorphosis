# Create your views here.

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from metamorphosis.settings.base import message_producer


class PingView(APIView):

    def get(self, request):
        return Response(
            status=status.HTTP_200_OK,
            data={
                "status": "up"
            },
        )


class SendKafkaEventView(GenericAPIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        message_producer.send(topic="pre_evaluation_finished", value="Hello, world!")
        return Response(
            status=status.HTTP_200_OK,
            data={"Hello": "World"}
        )
