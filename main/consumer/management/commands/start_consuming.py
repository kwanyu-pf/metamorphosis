import signal

from django.core.management.base import BaseCommand

from consumer.consumer import receive_message


def sigterm_handler(sig, frame):
    print(f"END Consumer {sig}")
    exit(0)


class Command(BaseCommand):
    help = "Start Listener"

    def handle(self, *args, **options):
        signal.signal(signal.SIGTERM, sigterm_handler)

        receive_message()
