from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import redirect


def index(request):
    if request.user.is_authenticated:
        return redirect('business_dashboard')
    else:
        return render(request,"quickbizz/index.html")
