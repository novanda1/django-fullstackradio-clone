from dango.apps.podcast.documents import PodcastDocument
from django.shortcuts import render


def search(request):
    query = request.GET.get('q', '')
    sqs_app = PodcastDocument.search().query(
        "multi_match", query=query, fields=["id", "title", "excerpt"])
    podcast = sqs_app.to_queryset()

    context = {
        "result": podcast,
        "text": 'oke broh'
    }
    template_name = "msearch/result.html"

    return render(request, template_name, context)
