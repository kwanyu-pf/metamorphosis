from confluent_kafka import SerializingProducer
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView


class PingView(GenericAPIView):
    pass


class SendKafkaEventView(GenericAPIView):
    producer = SerializingProducer()
