from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from dev.forms import MessageForm, SignUpForm, UserProfileForm, StatusForm, DiscussionForm
from dev.models import Message, UserProfile, Status, Discussion
from django.contrib.auth.models import User
import datetime

# Create your views here.

def index(request):
    user = request.user
    context_dict = {}
    if user.is_authenticated():
        context_dict = {"welcome": user}
    else:
        context_dict = {"welcome": "User"}
    return render(request, 'dev/base.html', context_dict)

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
        form = UserProfileForm(initial={'email': request.user.email})
    return render(request, 'dev/profile.html', {'form': form})

def show_profile(request, username):
    user = User.objects.get(username=username)
    prof = UserProfile.objects.get(user=user)
    return render(request, 'dev/show_profile.html', {"profile": prof, "user": user})

# def message_list(request, username):
#     user = User.objects.get(username=username)
#     form = MessageForm(initial={"reciever": user})
#     user = User.objects.get(username=username)
#     try:
#         message = Message.objects.get(reciever=user)
#     except Message.DoesNotExist:
#         return render(request, 'dev/message.html', {'form': form})
#     template = 'dev/message.html'
#
#     return render(request, template, {'message': message, "form": form})
#
# def send_message(request):
#     if request.method == 'POST':
#         username = request.POST.get('reciever')
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             msg = form.save(commit=False)
#             msg.sender = request.user.username
#             msg.save()
#             return redirect('/dev/message/username')
#         else:
#             print(form.errors)

def message_list(request, username):
    msglist = []
    sender = request.user.username
    form = MessageForm(initial={"reciever": username, "sender": sender})
    msg = {}
    context_dict = {'form': form}
    template = 'dev/message.html'
    try:
        sent = Message.objects.filter(reciever=username).filter(sender=sender).order_by('datetime')
        msg['sent'] = sent
        print "This has sent"
    except Message.DoesNotExist:
        print "This did not send"
    try:
        recieved = Message.objects.filter(reciever=sender, sender=username).order_by('datetime')
        msg['recieved'] = recieved
        print "This has recieved"
    except Message.DoesNotExist:
        pass
    for i in msg['sent']:
        msglist.append(i)
    for i in msg['recieved']:
        msglist.append(i)
    swaped = True
    while swaped:
        swaped = False
        for i in range(len(msglist)-1):
            if msglist[i].datetime > msglist[i+1].datetime:
                msglist[i], msglist[i+1] = msglist[i+1], msglist[i]
                swaped = True
    context_dict['both_msg'] = msglist
    return render(request, template, context_dict)


def send_message(request):
    reciever = request.POST.get('reciever')
    print reciever
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.reciever = reciever
            msg.sender = request.user.username
            msg.datetime = datetime.datetime.now()
            msg.save()
            return redirect("/dev/message/"+reciever)
        else:
            print(form.errors)


def friends(request):
    friends = User.objects.all()
    return render(request, 'dev/friends.html', {'friends': friends})



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
            dis.datetime = datetime.datetime.now()
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
