from django.conf.urls import url

from django.views.generic.base import RedirectView

from .views import (
    UserDetailView
    )

urlpatterns = [
    # url(r'^$', RedirectView.as_view(url="/")),
    # url(r'^search/$', TweetListView.as_view(), name='list'),
    # url(r'^create/$', TweetCreateView.as_view(), name='create'),
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/update/$', TweetUpdateView.as_view(), name='update'),
    # url(r'^(?P<pk>[0-9]+)/delete/$', TweetDeleteView.as_view(), name='delete'),
]

