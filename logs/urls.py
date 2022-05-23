"""Define padrões de URL para learning_logs."""

from django.urls import path

from . import views

app_name = "logs"

urlpatterns = [
    path("", views.index, name="index"),
    path("topics", views.topics, name="topics"),
    path("topics/<int:pk>", views.topic, name="topic"),
    # path("", index.as_view(), name="index"),
]
