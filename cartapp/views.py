from django.shortcuts import render
from .models import Destination

# Create your views here.

def home(request):
    
    dest = Destination.objects.all()
    
    return render(request, 'home.html', {'dest': dest})