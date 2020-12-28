from django.shortcuts import render

from .models import *

# Create your views here.
def users(request):
    context = {
        "users": Users.objects.all()
    }
    return render(request, 'index.html', context)