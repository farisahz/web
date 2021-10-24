from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

from .models import adminuser
from .forms import SignUpForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib import messages


import mysql.connector
from operator import itemgetter

# Create your views here.

def index(request):
    return render(request, 'index.html')


def dashboard (request):
    return render(request, 'dashboard.html')

def login (request):
    con = mysql.connector.connect(
        host = "localhost",
        user='root',
        password = "",
        database = "db_web_admin",
    )
    cursor = con.cursor()

    con2 = mysql.connector.connect(
        host = "localhost",
        user='root',
        password = "",
        database = "db_web_admin",
    )
    cursor2 = con2.cursor()

    sql_command = "SELECT username FROM adminwebsite_adminuser"
    sql_command2 = "SELECT password FROM adminwebsite_adminuser"
    cursor.execute(sql_command)
    cursor2.execute(sql_command2)
    
    uname=[]
    pwd=[]

    for i in cursor:
        uname.append(i)
        # list of username that registered

    for y in cursor2:
        pwd.append(y)
        # list of password
    print(uname)
    print(pwd)

    resource = list(map(itemgetter(0), uname))    
    resource2 = list(map(itemgetter(0), pwd))   

    print(resource) 

    if request.method == "POST":
        name = request.POST['username']
        password1 = request.POST['password']

        i=1
        k=len(resource)
        
        while i<k:
            if resource[i] == name and resource2[i] == password1:
                messages.success(request, f"Welcome, {name}")
                return redirect('dashboard')
                break
            i+=1

        else:
            messages.error(request, "Check username and password")
            return redirect('login')

    return render(request, 'registration/login.html')

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            pnum = form.cleaned_data.get('no_phone')
            pwd1 = form.cleaned_data.get('password')
            pwd2 = form.cleaned_data.get('password2')
            reg = adminuser(username=uname, email=email, no_phone=pnum, password=pwd1, password2=pwd2) 
            
            reg.save()
            
            messages.success(request, f"{uname}, your account have succesfully created")
            return redirect('login')
            
        else:
            form = SignUpForm()
            messages.error(request, "Please Try Again.")

    context={
        'form':SignUpForm
    }
    return render(request, 'registration/newregister.html', context)


def logout(request):
    auth_logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')




















'''
def signup (request):
    if request.method == "POST":
        user = adminuser()

        user.username = request.POST['username']
        user.email = request.POST['email']
        user.no_phone = request.POST['no_phone']
        user.password = request.POST['password']
        user.password2 = request.POST['password2']
        
        if user.password != user.password2:
            return redirect('signup')
        elif user.username == "" or user.password == "":
            messages.info(request, 'missing')
            return redirect('signup')

        else:
            user.save()


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Success")
            return redirect('login')
        else:
            form = SignUpForm()
            messages.error(request, 'Unsuccessful Registration.')

    return render(request, "signup.html")

   
    user = request.user
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    con = mysql.connector.connect(
        host = "localhost",
        user='root',
        password = "",
        database = "db_web_admin",
    )
    cursor = con.cursor()

    con2 = mysql.connector.connect(
        host = "localhost",
        user='root',
        password = "",
        database = "db_web_admin",
    )
    cursor2 = con2.cursor()

    sqlcommand = "select username from adminwebsite_adminuser"
    sqlcommand2 = "select password from adminwebsite_adminuser"

    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand2)
    e=[]
    p=[]

    
    for i in cursor:
        e.append(i)

    for i in cursor2:
        p.append(i)

    res = list(map(itemgetter(0), e))
    res2 = list(map(itemgetter(0), p))
    print(res)

    if request.method == "POST":
        name = request.POST['username']
        password1 = request.POST['password']

        i=1
        k = len(res)
        while i < k:
            if res[i] == name and res2[i] == password1:
                return render(request, 'dashboard.html', {'username':name})
                break
            i+=1

        else:
            messages.info(request, "Check username or password")
            return redirect('login')

    return render(request, 'registration/newlogin.html')
    '''