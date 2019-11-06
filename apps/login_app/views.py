from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# from django.db.models import Q
from .models import User

import bcrypt
from datetime import datetime, timedelta

# Landing Page: Localhost:8000/
def index(request):
    context = {
        'logged_in_users' : User.objects.all()
    }
    return render(request, "login_app/login.html", context)

# Login Page: Localhost:8000/login
def pre_login(request):
    return render(request, "login_app/register.html")

#Register User: Localhost:8000/register
def register(request):

    #Validation Check
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        plain_text_password = request.POST['password']
        plain_text_conf_password = request.POST['confirmation_password']
        
        #Hash the plaintext password created
        hashed_password = bcrypt.hashpw(plain_text_password.encode(), bcrypt.gensalt())

        #If hashed password matches confirmation password, add user to db and move to success page
        if bcrypt.checkpw(plain_text_conf_password.encode(), hashed_password):
        
            #Add user to database if registration successful
            new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed_password)
            
            #Set session user_key to id
            request.session['active_user'] = new_user.id
            return redirect('/dashboard')
        else:
            return redirect('/')

#Login User: Localhost:8000/login 
def login(request):
    print("You hit the login request!")
    #Validation Check
    errors = User.objects.login_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
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
                print("Current user updated to: " + str(login_user.first_name) + str(login_user.last_name))
                return redirect('/dashboard')
            else:
                print("Invalid credentials")
                return redirect('/')
        else:
            return redirect('/')
    return redirect('/dashboard')

#Successful Login/Register: Localhost:8000/dashboard
def dashboard(request):

    #If an attempt is made to get to dashboard without logging in, redirect to landing page.
    if not 'active_user' in request.session:
        return redirect('/')

    return redirect("/notes")

#Logout User: Localhost:8000/logout
def logout(request):
    del request.session['active_user']
    return redirect('/')