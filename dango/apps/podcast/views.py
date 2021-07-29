from django.http.response import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from django.utils.translation import gettext as _


from .models import Episode, Host

class PodcastListView(ListView):
    queryset = Episode.objects.filter(status=1).order_by('-created')
    paginate_by = 3
    template_name = 'index.html'


class PodcastDetailView(DetailView):
    model = Episode
    template_name = 'podcast_detail.html'


def test_lang(request):
    return HttpResponse(_("i want to say ok"))
