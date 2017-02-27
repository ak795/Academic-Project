from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect,render_to_response
from .forms import RegistrationForm, LoginForm, SearchForm
from django.utils import timezone
from textblob import TextBlob
import urllib
import urllib2
import json

url = 'http://sentiment.vivekn.com/api/text/'

# Create your views here.

"""def main_page(request):
    return render(request , 'WebApp/main_page' , {})"""

@csrf_exempt
def main_page(request):
    if request.method == 'POST':
        val = SearchForm(request.POST)
        print val.errors.as_data()
        if val.is_valid():
            sp = {}
            get_sentiment =  val.cleaned_data['search_query']
            post_data = {'txt' : get_sentiment}
            result = urllib2.urlopen(url , urllib.urlencode(post_data))
            content = result.read()
            response_content = json.loads(content)
            sp['confidence'] = response_content['result']['confidence']
            sp['sentiment_value'] = response_content['result']['sentiment']
            sp['text'] = get_sentiment
            #print content
            get_sentiment = TextBlob(get_sentiment)
            value = get_sentiment.sentiment.polarity

            #situation_score = situation.situation_analysis(get_sentiment)
            #r = requests.get(situation_score, verify=False, timeout=10)

            #print situation_score



            return render_to_response('WebApp/main_page' , {'result' : sp})

    else:
        val = SearchForm()

    return render(request , 'WebApp/main_page' , {'value' : val})


def signup_btn(request):
    form = RegistrationForm()
    return render(request , 'WebApp/signup.html' , {'form' : form})

def login_btn(request):
    form = LoginForm()
    return render(request , 'WebApp/login.html' , {'form' : form})

def login(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            post = form.save(commit = False)
            post.username = request.user
            post.email = request.user
            post.password = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('main_page' , pk = post.pk)


    else:
        form = RegistrationForm()

    return render(request , 'WebApp/logout.html' , {})

def logout(request):
    return render(request , 'WebApp/logout.html' , {})