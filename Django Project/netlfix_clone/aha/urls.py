from django.urls import path
from . import views

url_patterns = [ path('',views.home, name='home'), path('subscription/<int:user_id>/',views.subscriptions,name = 'subscriptions'),]