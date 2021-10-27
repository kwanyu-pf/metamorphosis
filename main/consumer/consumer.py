from json import dumps

from django.conf import settings
from kafka import KafkaConsumer


def receive_message():
    consumer = KafkaConsumer(
        bootstrap_servers=[settings.KAFKA_BOOTSTRAP_ENDPOINT],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='kwanyu',
        value_deserializer=lambda x: dumps(x).encode('utf-8')
    )
    print(f"start subscribing")
    consumer.subscribe(["pre_evaluation_finished"])

    print(f"start consuming")

    for message in consumer:
        print(f"pre evaluation finished! {message}")
