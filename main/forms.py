from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  # AuthenticationForm を追加
from django import forms
from .models import User


class LoginForm(AuthenticationForm):
    pass

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email",)
from .models import Talk, User  # Talk を追加

# ...

class TalkForm(forms.ModelForm):
    class Meta:
        model = Talk
        fields = ("message",)
        # 以下を追加
class UsernameChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username",)
        labels = {"username": "新しいユーザー名"}
        help_texts = {"username": ""}
        # 以下を追加
class EmailChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)
        labels = {"email": "新しいメールアドレス"}