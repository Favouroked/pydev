from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from dev.models import Message, UserProfile, Status, Discussion

class MessageForm(forms.ModelForm):
    sender = forms.CharField(widget=forms.HiddenInput)
    reciever = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Message
        exclude = ('datetime',)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    last_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    email = forms.EmailField(max_length=254, help_text="Required, input a valid email address")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    website = forms.URLField(max_length=128, help_text="Enter your website", required=False)

    def clean(self):
        cleaned_data = self.cleaned_data
        website = cleaned_data.get('website')
        if website and not website.startswith('http://'):
            website = 'http://' + website
            cleaned_data['website'] = website

            return cleaned_data

    class Meta:
        model = UserProfile
        exclude = ('user',)

class StatusForm(forms.ModelForm):
    stat_pic = forms.ImageField(required=False)

    class Meta:
        model = Status
        exclude = ('uploader', 'stat_id',)

class DiscussionForm(forms.ModelForm):
    msg_pic = forms.ImageField(required=False)

    class Meta:
        model = Discussion
        exclude = ('sender', 'datetime',)