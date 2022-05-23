from django.shortcuts import render
from .models import Topic


def index(request):
    """A página inicial de Learning Log"""
    return render(request, "logs/index.html")


def topics(request):
    """Mostra todos os assuntos."""
    topics = Topic.objects.order_by("date_added")
    context = {"topics": topics}
    return render(request, "logs/topics.html", context)


def topic(request, pk):
    """Mostra um único assunto e todas as suas entradas."""
    topic = Topic.objects.get(id=pk)
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "logs/topic.html", context)
