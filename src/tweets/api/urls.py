from django.conf.urls import url
from django.views.generic.base import RedirectView
from .views import (
    RetweetAPIView,
    TweetCreateAPIView,
    TweetListAPIView
    )

 
urlpatterns = [
    # url(r'^$', RedirectView.as_view(url="/")),
    url(r'^$', TweetListAPIView.as_view(), name='list'), # /api/tweet/
    url(r'^create/$', TweetCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/retweet/$', RetweetAPIView.as_view(), name='retweet'),
    # url(r'^(?P<pk>[0-9]+)/$', TweetDetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/update/$', TweetUpdateView.as_view(), name='update'),
    # url(r'^(?P<pk>[0-9]+)/delete/$', TweetDeleteView.as_view(), name='delete'),
]
