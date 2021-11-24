from django.conf import settings
from django.shortcuts import render

# Create your views here.
from kafka import KafkaAdminClient
from rest_framework.views import APIView


class CreateTopicView(APIView):

    def get(self, request):
        client = KafkaAdminClient(
            bootstrap_servers=[settings.KAFKA_BOOTSTRAP_ENDPOINT],
        )

        client.create_topics(["pre_evaluation_finished"])