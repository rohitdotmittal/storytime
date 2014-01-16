# Create your views here.
#from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import Line, ZomatoItem, user_profile, FashionItem
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from .forms import user_profile_form, ProfileForm
from django.contrib.auth.decorators import login_required
import smtplib
from email.mime.text import MIMEText
#from .forms import RegistrationForm

def login(request):
    c = {}
    c.update(csrf(request))
    render_to_response("story/login.html", c) 

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/all_details', {'username':username})
    else:
        return HttpResponseRedirect('/invalid')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')
	
def loggedin():
    return render_to_response('loggedin.html', 
                              {'full_name': request.user.username})

def invalid_login():
    return render_to_response('invalid_login.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_success')
        else:
            return HttpResponseRedirect('/invalid_login')
        
    args = {}
    args.update(csrf(request))
        
    args['form'] = UserCreationForm()
    return render_to_response('story/register.html', args)

def register_success(request):
    return render_to_response('story/register_success.html')

def home_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_success')
        else:
            return HttpResponseRedirect('/invalid_login')

    args = {}
    args.update(csrf(request))
        
    args['form'] = UserCreationForm()
    return render_to_response('story/home_page.html', args)

@login_required
def profile_backup(request):
    if request.method == 'POST':
        form = user_profile_form(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/all_details')
        else:
            return HttpResponseRedirect('/home_page')
    else:
        user = request.user
        profile = user.profile
        form = user_profile_form(instance=profile)
    
'''
@login_required
def profile(request):
	if request.method == 'POST':
		form = user_profile_form(request.POST, instance=request.user.profile)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/all_details')
	else:
		user = request.user
		profile = user.profile
		form = user_profile_form(instance=profile)
	args = {}
	args.update(csrf(request))
	args['form'] = form
	args['user'] = user
	return render_to_response('story/profile.html', args)
	

'''


@login_required
def profile_update(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST, instance=request.user.profile)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.user = request.user
			profile.save()
			form.save_m2m() # needed since using commit=False
			return HttpResponseRedirect('/all_details')
	else:
		user = request.user
		profile = user.profile
		form = ProfileForm(instance=profile)
	args = {}
	args.update(csrf(request))
	args['form'] = form
	args['user'] = request.user
	return render_to_response('story/profile.html', args)
	

	
def restaurants(request):
    items_list = list(ZomatoItem.objects.filter(id__range = (1,11)))
    return render_to_response('story/restaurants.html', {'z_items' : items_list})

def games(request):
    return render_to_response('story/games.html')

def shopping(request):
    items_list = list(ZomatoItem.objects.filter(id__range = (1,11)))
    return render_to_response('story/shopping.html', {'s_items':items_list})


def home(request):
    language = 'en_gb'
    session_language = 'en_gb'

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    
    if 'lang' in request.session:
        session_language = request.session['lang']

    return render_to_response("story/home.html", {'lines': Line.objects.all(), 'language' : language, 'session_language' : session_language})

def zomato(request):
    return render_to_response("story/zomato.html", {'z_items' : ZomatoItem.objects.all()})

def language(request, language = 'en_gb'):
    response = HttpResponse("setting language to %s" % language)

    response.set_cookie('lang', language)

    request.session['lang'] = language

    return response

def activities(request):
    return render_to_response('story/activities.html', {'activities': ZomatoItem.objects.all().filter(activity__icontains="Activities")})

@login_required
def all_details(request, **kwargs):
    username = kwargs
    return render_to_response("story/all_details.html", {'z_items' : ZomatoItem.objects.all(), 'username':username})

def all_details(request, **kwargs):
    username = kwargs
    return render_to_response("story/all_details.html", {'z_items' : ZomatoItem.objects.all(), 'username':username})

def hunch_page(request):
    return render_to_response("story/hunch_page.html")

def sosh_page(request):
    return render_to_response("story/sosh_page.html")

def email_item(request):
    items_list = list(ZomatoItem.objects.filter(id__range = (1,11)))
    gmail_user = "rmittal@popsugar.com"
    gmail_pwd = ""
    FROM = 'rmittal@popsugar.com'
    TO = 'rohit.mittal.2006@gmail.com'
    SUBJECT = "Cool email from Rohit's site"
    TEXT = "Rohit came up with this cool idea about the site, take a look at it."
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, TO, SUBJECT, TEXT)

#server = smtplib.SMTP(SERVER) 
    server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pwd)
    server.sendmail(FROM, TO, message)
    #server.quit()
    server.close()

    return render_to_response('story/restaurants.html', {'z_items' : items_list})




"""
def importitems(request):
    f = open('/Users/rmittal/webapp/ENV/bin/storytime/initial_data.json', 'r')
    obj = json.load(f)
    for o in object:
        record = ZomatoItem
"""
