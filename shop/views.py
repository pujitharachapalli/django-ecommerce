from django.shortcuts import render,redirect
from .models import Product,Order,Registration
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.

def index(request):
    products = Product.objects.all()


    product_name = request.GET.get('item_name')
    if product_name != '' and product_name is not None:
        products = products.filter(title__icontains = product_name)

    paginator = Paginator(products,4)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request,'shop/index.html', {'products': products})

def detail(request,id):
    product = Product.objects.get(pk = id)
    return  render(request,'shop/detail.html', { 'product' : product})

def checkout(request):

    if request.method == "POST":
        items = request.POST.get('items','items')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zipcode = request.POST.get('zipcode','')
        total = request.POST.get('total','')
        order = Order(items=items,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode,total=total)
        order.save()
    return render(request,'shop/checkout.html')

def registration(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name','')
        last_name = request.POST.get('last_name','')
        user_name = request.POST.get('user_name','')
        email = request.POST.get('email','')
        password1 = request.POST.get('password1','')
        password2 = request.POST.get('password2','')

        if(password1 == password2):
            if Registration.objects.filter(user_name = user_name).exists():
                messages.info(request,'Username Taken')
                return redirect('registration')
            elif Registration.objects.filter(email = email).exists():
                messages.info(request,'Email exists')
                return redirect('registration')
            else:
                register = Registration(first_name=first_name,last_name=last_name,user_name=user_name,email=email,password1= password1,password2=password2)
                register.save()
                return redirect('/shop')
        else:
            messages.info(request,'Passwords are not matched')
            return redirect('registration')

        return redirect('/shop')
    else:
        return render(request, 'shop/registration.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect("/shop")
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    else:
        return render(request, 'shop/login.html')

def logout(request):
    auth.logout(request)
    return redirect("/shop")


   