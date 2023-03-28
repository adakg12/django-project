from django import forms
from first_app.models import UserProfileInfo
from django.contrib.auth.models import User

class UserInfo(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password','email')

class UserProfileInfoForm(forms.ModelForm):

    class Meta:

        model = UserProfileInfo

        fields = ('portfolio_url','profile_pic')        
    