from django.urls import path

from consumer.views import CreateTopicView
from producer.views import PingView, SendKafkaEventView

urlpatterns = [
    path('ping', PingView.as_view()),
    path('test-kafka', SendKafkaEventView.as_view()),
    path('create-topic', CreateTopicView.as_view()),
]