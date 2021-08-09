from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from dango.apps.podcast.models import Host, Episode


@registry.register_document
class PodcastDocument(Document):
    class Index:
        name = "podcasts"
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}
        description = fields.TextField(attr='get_description')

    class Django:
        model = Episode
        fields = [
            'title',
            'excerpt'
        ]
