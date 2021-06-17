from plotly.offline import plot
from django.shortcuts import render, redirect

from . import models
from .forms import UserForm, RegisterForm, PPGForm
from .utils import plot




def index(request):
    pass
    return render(request, 'index.html')


def login(request):
    if request.session.get('is_login', None):
        return redirect('/uploadppg/')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "Check inputs!"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/uploadppg/')
                else:
                    message = "Wrong Password!"
            except:
                message = "Username is not existed!"
        return render(request, 'login.html', locals())

    login_form = UserForm()
    return render(request, 'login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('/uploadppg/')
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "Check inputs!"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:
                message = "Password is different!"
                return render(request, 'register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = 'Username existed！'
                    return render(request, 'register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = 'Email has already been used!'
                    return render(request, 'register.html', locals())

                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')
    register_form = RegisterForm()
    return render(request, 'register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")
    request.session.flush()
    return redirect("/login/")


def SavePPG(request):
    saved = False
    message = ""
    plot_html = "abcde"

    if request.method == "POST":
        MyPPGForm = PPGForm(request.POST, request.FILES)

        if MyPPGForm.is_valid():
            ppg = models.PPG()
            ppg.name = MyPPGForm.cleaned_data["name"]
            ppg.ppgdata = MyPPGForm.cleaned_data["ppgdata"]
            if ppg.ppgdata.name.split(".")[-1].lower() == "csv":
                ppg.save()
                saved = True
                plot_html = plot(ppg.ppgdata.path)
            else:
                message = "Not .csv file. "
    else:
        MyPPGForm = PPGForm()
        message = "Failed. "

    return render(request, 'saved.html', locals())

def about(request):
    pass
    return render(request, 'about.html')

