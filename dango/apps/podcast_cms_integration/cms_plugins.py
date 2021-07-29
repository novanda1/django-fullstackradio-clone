from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import PodcastPluginModel
from django.utils.translation import gettext as _
from cms.models.pluginmodel import CMSPlugin
from dango.apps.podcast.models import Episode


@plugin_pool.register_plugin
class PodcastPluginPublisher(CMSPluginBase):
    model = PodcastPluginModel
    module = _("Podcast")
    name = _("Podcast Plugin")
    render_template = "podcast_cms_integration/podcast_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


@plugin_pool.register_plugin
class PodcastListPluginPublisher(CMSPluginBase):
    model = CMSPlugin
    module = _("Podcast")
    render_template = "podcast_cms_integration/podcast_list_plugin.html"
    name = _("Podcast List")

    def render(self, context, instance, placeholder):
        placeholder = Episode.objects.filter(status=1).order_by('-created')[:1]
        context = super().render(context, instance, placeholder)
        return context
