from rest_framework import serializers
from django.utils.timesince import timesince
from accounts.api.serializers import UserDisplaySerializer
from tweets.models import Tweet

class ParentTweetModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True) #write_onlyasd
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    
    class Meta:
        model = Tweet
        fields = [
            'id',
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince',
        
        ]

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d, %Y at %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + " ago"

class TweetModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True) #write_onlyasd
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    parent = ParentTweetModelSerializer(read_only=True)
    class Meta:
        model = Tweet
        fields = [
            'id',
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince',
            'parent',
        ]

    def get_is_retweet(self, obj):
        if obj.parent:
            return True
        return False

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d, %Y at %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + " ago"