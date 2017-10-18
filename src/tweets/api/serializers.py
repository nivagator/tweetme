from rest_framework import serializers
from django.utils.timesince import timesince
from accounts.api.serializers import UserDisplaySerializer
from tweets.models import Tweet

class ParentTweetModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True) #write_onlyasd
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    # did_like = serializers.SerializerMethodField()
    class Meta:
        model = Tweet
        fields = [
            'id',
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince',
            'likes',
            # 'did_like',
        ]

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d, %Y at %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + " ago"

    def get_likes(self, obj):
        return obj.liked.all().count()
    
    # def get_did_like(self, obj):
    #     request = self.context.get("request")
    #     user = request.user
    #     if user.is_authenticated():
    #         if user in obj.liked.all():
    #             return True
    #     return False

class TweetModelSerializer(serializers.ModelSerializer):
    parent_id = serializers.CharField(write_only=True, required=False)
    user = UserDisplaySerializer(read_only=True) #write_onlyasd
    date_display = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    did_like = serializers.SerializerMethodField()
    parent = ParentTweetModelSerializer(read_only=True)
    class Meta:
        model = Tweet
        fields = [
            'id',
            'parent_id',
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince',
            'parent',
            'likes',
            'did_like',
            'reply',
        ]
        # read_only_fields = ['reply']

    def get_did_like(self, obj):
        request = self.context.get("request")
        user = request.user
        if user.is_authenticated():
            if user in obj.liked.all():
                return True
        return False

    def get_is_retweet(self, obj):
        if obj.parent:
            return True
        return False

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d, %Y at %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + " ago"

    def get_likes(self, obj):
        return obj.liked.all().count()