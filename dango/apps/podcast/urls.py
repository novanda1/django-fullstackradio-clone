from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('', views.PodcastListView.as_view(), name="list"),
    path('<int:pk>/', views.PodcastDetailView.as_view(), name="detail"),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    path('test/', views.test_lang)
]

# urlpatterns += i18n_patterns(
#     path('', views.PodcastListView.as_view(), name='index'),
#     path('<int:pk>/', views.PodcastDetailView.as_view(), name='detail'),
#     path('test/', views.test_lang)
# )
