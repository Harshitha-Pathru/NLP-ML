from django.shortcuts import render
from .models import User, Movie,Subscription

def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html') ,{'movies' : movies}
def subscription(request,user_id):
    user = User.objects.get(id = user_id)
    subscriptions = Subscription.objects.filter(user = user)
    return render(request, 'subscriptions.html', {'subscriptions': subscriptions , 'user' : user})
