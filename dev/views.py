from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from dev.forms import MessageForm, SignUpForm, UserProfileForm
from dev.models import Message, UserProfile
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    user = request.user
    context_dict = {}
    if user.is_authenticated():
        context_dict = {"welcome": user}
    else:
        context_dict = {"welcome": "User"}
    return render(request, 'dev/base.html', context_dict)

def message(request):
    sender = request.user.username
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = sender
            msg.save()
            return redirect('/')
        else:
            print(form.errors)
    else:
        form = MessageForm()
    context_dict = {'form': form}
    return render(request, 'dev/message.html', context_dict)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'dev/signup.html', {'form': form})
def user_list(request):
    the_list = User.objects.all()
    context_dict = {"users": the_list}
    return render(request, "dev/people.html", context_dict)

def update_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect('/')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'dev/profile.html', {'form': form})

def show_profile(request, username):
    user = User.objects.get(username=username)
    prof = UserProfile.objects.get(user=user)
    return render(request, 'dev/show_profile.html', {"profile": prof, "user": user})