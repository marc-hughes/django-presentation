from django.db import models

# Create your models here.
class InterestingPerson( models.Model ):
    name = models.CharField(max_length=80)
    twitter_username = models.CharField(max_length=80)
    follow_count = models.IntegerField(default=0)
    picture_url = models.URLField()