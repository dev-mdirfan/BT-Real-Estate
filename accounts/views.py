from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
# Create your views here.

def register(request):
    if request.method == 'POST':
        # Get Form Values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Validation - Check if password match
        if password == password2:
            # Username Validation
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
                return redirect('register')
            else:
                # Email Validation
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already being used.')
                    return redirect('register')
                else:
                    # Everything Looks Good
                    user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                    # Login After Register
                    # First Method
                    # auth.login(request, user)
                    # messages.success(request, 'You are now registered and can log in.')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'You are now registered and can log in.')
                    return redirect('login')
        else:
            # Register User
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        # Login User
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out.')
        return redirect('index')

def dashboard(request):
    # Get Contacts of the inquiry of logged in users
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)