from typing import List

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class PodcastAppHook(CMSApp):
    app_name = 'Podcast'
    name = 'Podcast Application'

    def get_urls(self, *args, **kwargs) -> List[str]:
        return ["dango.apps.podcast.urls"]
