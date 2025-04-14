from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import business_profile
from .models import Product
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

#main page  of businessess where information will be shown to everyone..

def business_index(request):
    return render(request,'businesses/business_index.html')


@login_required(login_url='business_login') 
def business_dashboard(request):
    business = business_profile.objects.get(user=request.user)
    return render(request, 'businesses/business_dashboard.html', {'business': business})



@login_required(login_url='business_login')
def business_profile_view(request,username):
    business = business_profile.objects.get(user=request.user, user__username=username)
    return render(request,'businesses/business_profile.html',{'business':business})


@login_required
def add_product(request):
    if request.method=='POST':

        #Getting Form data from front end
        product_name=request.POST.get('product_name')
        product_description=request.POST.get('product_description')
        product_price=request.POST.get('product_price')
        product_image=request.FILES.get('product_image') 
        is_available=request.POST.get('is_available') =='on'

        #Now here we are mapping this data with business profile valid
        business=business_profile.objects.get(user=request.user)

        #Here we are adding the form information to the database or models.
        product=Product.objects.create(
            business=business,
            product_name=product_name,
            product_description=product_description,
            product_price=product_price,
            product_image=product_image,
            is_available=is_available
        )
        if product is not None:
            messages.success(request,"Product Added Successfully")
            return redirect('business_dashboard')
        else:
            messages.error(request,"Product Not Added")
            return render(request,'businesses/add_product.html')
    return render(request,'businesses/add_product.html')
    

@login_required(login_url='business_login')

def products_list(request):

    business= business_profile.objects.get(user=request.user)

    products_list= Product.objects.filter(business=business)

    return render(request,'businesses/products_list.html',{'products_list':products_list})




@login_required(login_url='business_login')
def view_business_products(request,username):

    
    business=get_object_or_404(business_profile,business_name__iexact=username)
    products=Product.objects.filter(business=business)
    return render(request, 'businesses/business_view_products.html', {
        'products': products,
        'business': business
    })



def business_index(request):
    business=business_profile.objects.all()
    return render(request,'businesses/business_index.html',{'business':business})

def business_register(request):
    if request.method=='POST':
       
       #Getting Form data from front end
       #here we have used built in username and password of django User auth.

       username=request.POST['username']
       password=request.POST['password']
       confirm_password=request.POST['confirm_password']
    
       business_name = request.POST['business_name']
       business_email = request.POST['business_email']
       business_num = request.POST['business_num']
       business_location = request.POST['business_location']
       business_category = request.POST['business_category']
       business_logo = request.FILES.get('business_logo') 
       opening_time = request.POST['opening_time']
       closing_time = request.POST['closing_time']

       #here  we are trying to match user given both passwords if they are equal we will proceed further
       if password != confirm_password:
            messages.error(request,"Passwords do not match TRY AGAIN")
            return render(request,'businesses/business_signup.html')
       
       #Checking is username available
       if User.objects.filter(username=username):
           messages.error(request,"Username Already Exists!")
           return render(request,'businesses/business_signup.html')
       

       #Saving the User with auth

       user=User(username=username)
       user.set_password(password) # Securely hash the password
       user.save()

       #now link everything to the User in Database

       business = business_profile.objects.create(
           user=user,
           business_name=business_name,
           business_email=business_email,
           business_num=business_num,
           business_location=business_location,
           business_category=business_category,
           business_logo=business_logo,
           opening_time=opening_time,
           closing_time=closing_time
           
       )

       messages.success(request,"Successfully Registered")
       return redirect('business_login')  # Redirect to login page after successful registration
    
    return render (request,'businesses/business_signup.html')


def business_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('business_dashboard')  # Redirect to the business index page after successful login

        else :
            messages.error(request,"Invalid Credentials")
    return render(request,'businesses/business_signin.html')


def business_logout(request):
    logout(request)
    return redirect('business_login')