from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
from datetime import datetime, timedelta
import bcrypt

def index(request):
    return render(request, "login_app/login.html")

def register_page(request):
    return render(request, "login_app/register.html")

def register(request):
    #Validation Check
    errors = User.objects.registration_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, key)
        return redirect('/registration')
    else:
        plain_text_password = request.POST['password']
        plain_text_conf_password = request.POST['confirmation_password']
        
        #Hash the plaintext password created
        hashed_password = bcrypt.hashpw(plain_text_password.encode(), bcrypt.gensalt())

        #If hashed password matches confirmation password, add user to db and move to success page
        if bcrypt.checkpw(plain_text_conf_password.encode(), hashed_password):
        
            #Check to see if the email entered is unique
            matches = User.objects.filter(email=request.POST['email'])

            if len(matches) > 0 :
                messages.error(request, "Email already exists", extra_tags="email")
                return redirect('/registration')
            else:
                #Add user to database if registration successful
                new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed_password)
            
                #Set session active_user to id of new user object
                request.session['active_user'] = new_user.id
            return redirect('/dashboard')
        else:
            return redirect('/')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, key)
        return redirect('/')
    else:
        if User.objects.filter(email=request.POST['email']):
            user_email = request.POST['email']
            user_password = request.POST['password']

            login_user = User.objects.get(email=user_email)
            login_user_password = request.POST['password']

            passwords_match = bcrypt.checkpw(login_user_password.encode(), login_user.password.encode())
            if passwords_match:
                request.session['active_user'] = login_user.id
                return redirect('/dashboard')
            else:
                messages.error(request, "Incorrect email or password", extra_tags="password")
                return redirect('/')
        else:
            return redirect('/')
    return redirect('/dashboard')

def login_as_guest(request):
    found_guest = User.objects.filter(first_name="Guest")
    if(len(found_guest) > 0):
        print("Guest account found.")
        request.session['active_user'] = found_guest[0].id
    else:
        print("New Guest account created.")
        new_user = User.objects.create(first_name='Guest', last_name='User', email='GuestUser@Ege.com', password='password')
        request.session['active_user'] = new_user.id

    return redirect('/dashboard')

def dashboard(request):

    #If an attempt is made to get to dashboard without logging in, redirect to landing page.
    if 'active_user' not in request.session:
        return redirect('/')
    
    #If user successfully gets to the dashboard, redirect to dashboard page of the note app.
    return redirect("/notes")

def logout(request):
    request.session.clear()
    # del request.session['active_user']
    return redirect('/')