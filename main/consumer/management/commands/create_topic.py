from django.conf import settings
from django.core.management import BaseCommand
from kafka import KafkaAdminClient


class Command(BaseCommand):
    def handle(self, *args, **options):
        client = KafkaAdminClient(
            bootstrap_servers=[settings.KAFKA_BOOTSTRAP_ENDPOINT],
        )

        client.create_topics(["pre_evaluation_finished"])
