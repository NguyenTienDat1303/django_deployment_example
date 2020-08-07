from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from first_app.models import Topic, Webpage, AccessRecord, User
from first_app.forms import FormName, NewUser, UserProfileInform
from django.contrib.auth.models import User as AdminUser
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    return render(request, 'first_app/index.html')


def form_name_view(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            print("VALIDATION_SUCCESS!")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])

    return render(request, 'first_app/form_page.html', {'form': form})


def user_list(request):
    list_user = User.objects.all().order_by('first_name')
    user_dict = {'users': list_user}
    return render(request, 'user.html', context=user_dict)


def sign_up(request):
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return user_list(request)
        else:
            print('ERROR FORM INVALID')
    return render(request, 'first_app/login.html', {'form': form})


def register(request):
    registered = False
    if request.method == "POST":
        user_form = NewUser(data=request.POST)
        profile_form = UserProfileInform(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = NewUser()
        profile_form = UserProfileInform()

    return render(request, 'two_app/registration.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print("Some tried to login and failed")
            print("Username: {} and password: {}".format(username, password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request, 'two_app/login.html')

@login_required
def special(request):
    return HttpResponse('You are logged in, Nice!')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))