from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^signup/$' , views.signup_btn , name = 'signup_btn'),
    url(r'^login/$' , views.login_btn , name = 'login_btn'),
    url(r'^logout/$' , views.logout , name = 'logout'),
    url(r'^$' , views.main_page , name = 'main_page') ,  #this pattern will tell django that views,main_page is the right place to go
]