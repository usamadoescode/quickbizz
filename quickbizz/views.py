from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from businesses.models import business_profile

def index(request):
    if request.user.is_authenticated:
        return redirect('business_dashboard')
    
    return render(request,"quickbizz/index.html")
