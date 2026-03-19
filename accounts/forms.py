from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Логин'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Пароль'})
        self.fields['password2'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Повторите пароль'})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'phone', 'avatar', 'bio', 'roblox_username']
        widgets = {
            'nickname': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ник в игре'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '+7...'}),
            'avatar': forms.FileInput(attrs={'class': 'form-file', 'accept': 'image/*'}),
            'bio': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 3, 'placeholder': 'О себе...'}),
            'roblox_username': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Roblox username'}),
        }
        labels = {
            'nickname': 'Никнейм',
            'phone': 'Телефон',
            'avatar': 'Фото профиля',
            'bio': 'О себе',
            'roblox_username': 'Roblox Username',
        }
