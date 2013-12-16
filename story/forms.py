#!/usr/bin/env python
from django import forms
from .models import Choices, Profile
from django.contrib.auth.models import User
from .models import user_profile
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        # user.set_password(self.cleaned_data['password1'])
        
        if commit:
            user.save()
            
        return user

class user_profile_form(forms.ModelForm):

    class Meta:
        model = user_profile
        fields = ('restaurants','date_night','family_dinner','on_a_Budget','video_games','xbox','PS','PC','gender','shopping','best_deals','daily_picks','art','art_galleries','design','technology','latest_phones','electronics','mobile_phones','tvs'
                  ,'home_theater','fashion','clothes','accessories','shoes','clubs','dance_clubs','bars','sports_bars','dive_bars','pubs')
    

class ProfileForm(forms.ModelForm):
	the_choices = forms.ModelMultipleChoiceField(queryset=Choices.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)

	class Meta:
		model = Profile
		exclude = ['user']
		
	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
