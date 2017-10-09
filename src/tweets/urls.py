from django.conf.urls import url
from .views import (
    TweetCreateView,
    TweetDetailView, 
    TweetListView
)

urlpatterns = [
    url(r'^$', TweetListView.as_view(), name='list'),
    url(r'^create/$', TweetCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/$', TweetDetailView.as_view(), name='detail'),

]
