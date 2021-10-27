import signal

from django.core.management import BaseCommand

from consumer.consumer import receive_message


def sigterm_handler(sig, frame):
    print(f"END Consumer {sig}")
    exit(0)


class Command(BaseCommand):
    def handle(self, *args, **options):
        signal.signal(signal.SIGTERM, sigterm_handler)

        receive_message()
