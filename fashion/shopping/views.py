from django.shortcuts import render
from shopping.models import Product
from shopping.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from shopping.forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    product_objects = Product.objects.all()
    
   #srch code
    item_value = request.GET.get('item_value')
    if item_value !='' and item_value is not None:
     product_objects= product_objects.filter(title__icontains = item_value)

        
    #paginator code
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
        
    return render(request ,'index.html',{"product_objects":product_objects})

def detail(request,id):
    product_object=Product.objects.get(id=id)
    return render(request ,'detail.html',{"product_object":product_object})

# def test(request):
#     product_object=Product.objects.get(id=id)
#     return render(request ,'test.html',{"product_object":product_object})

def test(request):
    product_object=Product.objects.all()
    return render(request,'test.html',{"product_object":product_object})

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        # form = CustomUserCreationForm(request.POST)
        # if form.is_valid():
            # Save the user and log them in
            #user = form.save()
            # login(request, user)
            username = request.POST.get('username',)
            password = request.POST.get('password',)
            email = request.POST.get('email',)
            user= User(username=username, password=password,email=email)
            user.save()
            t1 = loader.get_template('index.html')
            return HttpResponse(t1.render())# Replace 'home' with the name of your hom
    else:
        form = CustomUserCreationForm()
    
    return render(request,'signup.html',{''})

def loginin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.') 
            return redirect('home') # Redirect to your home page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'loginin.html')
    


