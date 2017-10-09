from rest_framework import generics
from tweets.models import Tweet
from .serializers import TweetModelSerializer

class TweetListAPIView(generics.ListAPIView):
    # queryset = Tweets.objects.all()
    serializer_class = TweetModelSerializer
    # permission_classes = (IsAdminUser,)
    
    def get_queryset(self):
        return Tweet.objects.all()
