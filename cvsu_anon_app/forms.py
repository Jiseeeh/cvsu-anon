from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder' : 'Username'}), help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
        
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(RegisterForm,self).__init__(*args, **kwargs)
        
        self.fields['username'].label = ''
        self.fields['username'].help_text = 'Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'
        
        self.fields['password1'].widget.attrs['class'] = 'form-input'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].help_text = '<ul class="password-tips"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
        
        
        self.fields['password2'].widget.attrs['class'] = 'form-input'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].help_text = 'Enter the same password as before, for verification.'	
        