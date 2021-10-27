from django.urls import path

from producer.views import PingView, SendKafkaEventView

urlpatterns = [
    path('ping', PingView.as_view()),
    path('test-kafka', SendKafkaEventView.as_view())
]