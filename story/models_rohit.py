from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Line(models.Model):
    text = models.CharField(max_length=255)

    def __unicode__(self):
        return self.text


class ZomatoItem(models.Model):
    name = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    rating_value = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    recommendations = models.CharField(max_length=255)
    rating_scale = models.CharField(max_length=255)
    rating_value = models.CharField(max_length=255)
    highlights = models.CharField(max_length=255)
    cuisines = models.CharField(max_length=255)
    opening_times = models.CharField(max_length=255)
    happy_hours = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    buffet = models.CharField(max_length=255)
    images = models.TextField()
#    activity = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class user_profile(models.Model):
    user = models.OneToOneField(User)
    likes_shopping = models.BooleanField()
    favorite_res_name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.user

User.profile = property(lambda u: user_profile.objects.get_or_create(user=u)[0])
