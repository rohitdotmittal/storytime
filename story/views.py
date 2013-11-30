# Create your views here.
#from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import Line, ZomatoItem, user_profile
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from .forms import user_profile_form
from django.contrib.auth.decorators import login_required
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

def logout():
    auth.logout(request)
    return render_to_response('logout.html')

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
def profile(request):
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
    
def restaurants(request):
    return render_to_response('story/restaurants.html')



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

def all_details(request, **kwargs):
    username = kwargs
    return render_to_response("story/all_details.html", {'z_items' : ZomatoItem.objects.all(), 'username':username})

def hunch_page(request):
    return render_to_response("story/hunch_page.html")

def sosh_page(request):
    return render_to_response("story/sosh_page.html")





"""
def importitems(request):
    f = open('/Users/rmittal/webapp/ENV/bin/storytime/initial_data.json', 'r')
    obj = json.load(f)
    for o in object:
        record = ZomatoItem
"""
