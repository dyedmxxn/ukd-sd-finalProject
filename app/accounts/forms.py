from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')

        labels = {
            'username': 'Username:',
            'email': 'Email:',
        }
        widgets = {
            'username': forms.TextInput(),
            'email': forms.EmailInput(),
        }

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')