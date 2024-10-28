# myapp/views.py
from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def subscriptions(request, user_id):
    user = User.objects.get(id=user_id)
    subscriptions = Subscription.objects.filter(user=user)
    return render(request, 'subscriptions.html', {'subscriptions': subscriptions, 'user': user})
