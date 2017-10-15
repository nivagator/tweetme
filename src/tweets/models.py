from django.conf import settings
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

# Create your models here.
from .validators import validate_content

class TweetManager(models.Manager):
    def retweet(self, user, parent_obj):
        if parent_obj.parent:
            og_parent = parent_obj.parent
        else:
            og_parent = parent_obj

        qs = self.get_queryset().filter(
            user=user, parent=og_parent
            )
            
        if qs.exists():
            return None

        obj = self.model(
            parent = parent_obj,
            user = user,
            content = parent_obj.content,
        )
        obj.save()
        return obj

class Tweet(models.Model):
    # missing association to user
    parent      = models.ForeignKey("self", blank=True, null=True)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL)
    content     = models.CharField(max_length=140, validators=[validate_content])
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = TweetManager()

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse("tweet:detail", kwargs={"pk":self.pk})
    # def clean(self, *args, **kwargs):
    #     content = self.content
    #     if content == "abc":
    #         raise ValidationError("Content: Cannot be ABC")
    #     return super(Tweet, self).clean(*args, **kwargs)

    class Meta:
        ordering = ['-timestamp']
