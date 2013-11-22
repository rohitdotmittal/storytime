from django.db import models

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

