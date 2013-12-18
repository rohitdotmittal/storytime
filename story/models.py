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

class FashionItem(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    images = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.name

class user_profile(models.Model):
	user = models.OneToOneField(User)

	#likes_shopping = models.BooleanField()
	#favorite_res_name = models.CharField(max_length=100)
	#Restaurants
	restaurants = models.BooleanField()
	date_night = models.BooleanField()
	family_dinner = models.BooleanField()
	on_a_Budget = models.BooleanField()
	#Video Games
	video_games = models.BooleanField()
	xbox = models.BooleanField()
	PS = models.BooleanField()
	PC = models.BooleanField()
	#Gender
	gender = models.BooleanField()
	#Shopping - Best Deals/Daily Picks/
	shopping = models.BooleanField()
	best_deals = models.BooleanField()
	daily_picks = models.BooleanField()

	#Art - Art Galleries/Design
	art = models.BooleanField()
	art_galleries = models.BooleanField()
	design = models.BooleanField()

	#Technology - Latest Phones/
	technology = models.BooleanField()
	latest_phones = models.BooleanField()

	#Electronics - Mobile Phones/TVs/Home Theater
	electronics = models.BooleanField()
	mobile_phones = models.BooleanField()
	tvs = models.BooleanField()
	home_theater = models.BooleanField()

	#Fashion - Clothes/Accessories/Shoes
	fashion = models.BooleanField()
	clothes = models.BooleanField()
	accessories = models.BooleanField()
	shoes = models.BooleanField()

	#Clubs - Dance Clubs
	clubs = models.BooleanField()
	dance_clubs = models.BooleanField()

	#Bars - Sports bars/Dive bars/Pubs
	bars = models.BooleanField()
	sports_bars = models.BooleanField()
	dive_bars = models.BooleanField()
	pubs = models.BooleanField()
	
class Choices(models.Model):
	description = models.CharField(max_length=300)

	def __unicode__(self):
		return u'%s' % (self.description)
		
class Profile(models.Model):
	user = models.ForeignKey(User, blank=True, unique=True, verbose_name='user')
	#user = models.ForeignKey(User, blank=True, verbose_name='user')
	the_choices = models.ManyToManyField(Choices)
User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
	