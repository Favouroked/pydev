from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from dev.models import Message

class MessageForm(forms.ModelForm):
    subject = forms.CharField(max_length=128, help_text="Enter the subject of the message")
    reciever = forms.ModelChoiceField(User.objects.all())
    sender = forms.CharField(max_length=128, widget=forms.HiddenInput(), required=False)
    message = forms.TextInput()

    class Meta:
        model = Message
        fields = ('subject', 'message')

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    last_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    email = forms.EmailField(max_length=254, help_text="Required, input a valid email address")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'password1', 'password2')