from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from dev.forms import MessageForm, SignUpForm, UserProfileForm, StatusForm, DiscussionForm
from dev.models import Message, UserProfile, Status, Discussion
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
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            k = form.save(commit=False)
            k.user = request.user
            k.save()
            return redirect('/')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'dev/profile.html', {'form': form})

def show_profile(request, username):
    user = User.objects.get(username=username)
    prof = UserProfile.objects.get(user=user)
    return render(request, 'dev/show_profile.html', {"profile": prof, "user": user})

def status(request):
    status = Status.objects.all()
    form = StatusForm()
    context_dict = {"status": status, 'form': form}
    return render(request, "dev/status.html", context_dict)

def upload_status(request):
    status_id = 0
    if request.method == 'POST':
        form = StatusForm(request.POST, request.FILES)
        if form.is_valid():
            status_id += 1
            stat = form.save(commit=False)
            stat.uploader = request.user.username
            stat.stat_id = status_id
            stat.save()
            return redirect('/dev/status/')
        else:
            print(form.errors)
    else:
        form = StatusForm()
    return render(request, 'dev/upload_status.html', {'form': form})

def send_discus(request):
    if request.method == 'POST':
        form = DiscussionForm(request.POST, request.FILES)
        if form.is_valid():
            dis = form.save(commit=False)
            dis.sender = request.user.username
            dis.save()
            return redirect('/dev/show_msg/')
        else:
            print(form.errors)
    else:
        form = DiscussionForm()
    return render(request, 'dev/discussion.html', {'form': form})

def show_discus(request):
    msg = Discussion.objects.all()
    form = DiscussionForm()
    context_dict = {'msg': msg, 'form': form}
    return render(request, 'dev/discussion.html', context_dict)