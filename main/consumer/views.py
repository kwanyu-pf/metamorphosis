from django.conf import settings
from django.shortcuts import render

# Create your views here.
from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from rest_framework.views import APIView


class CreateTopicView(APIView):

    def get(self, request):
        client = KafkaAdminClient(
            bootstrap_servers=[settings.KAFKA_BOOTSTRAP_ENDPOINT],
        )
        topics = [NewTopic(name="pre_evaluation_finished", num_partitions=1, replication_factor=1)]
        client.create_topics(new_topics=topics)