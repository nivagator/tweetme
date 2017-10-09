from django.conf.urls import url
from .views import (
    TweetCreateView,
    TweetDeleteView,
    TweetDetailView, 
    TweetListView,
    TweetUpdateView
)

urlpatterns = [
    url(r'^$', TweetListView.as_view(), name='list'),
    url(r'^create/$', TweetCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/$', TweetDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', TweetUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', TweetDeleteView.as_view(), name='delete'),
]
