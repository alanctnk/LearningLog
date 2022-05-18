"""Define padrões de URL para learning_logs."""

from django.urls import path

from . import views


urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    # path("", index.as_view(), name="index"),
]
