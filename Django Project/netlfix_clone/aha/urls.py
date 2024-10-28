from django.urls import path
from . import views
'''
urlpatterns = [
    path('', views.home, name='home'),
    path('subscriptions/<int:user_id>/', views.subscriptions, name='subscriptions'),
]

'''

urlpatterns = [
    path('', views.home, name='home'),
]
