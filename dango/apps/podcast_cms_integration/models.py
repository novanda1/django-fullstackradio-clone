from dango.apps.podcast.views import PodcastListView
from django.db import models
from cms.models import CMSPlugin
from dango.apps.podcast.models import Episode, Host


class PodcastPluginModel(CMSPlugin):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    host = models.ForeignKey(
        Host, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.episode.title
