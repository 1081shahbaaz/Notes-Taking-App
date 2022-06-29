from django import forms

from django.contrib.auth.models import User
from .models import Profile


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control mb-3','style':'padding:3px ;'}))
    email = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control mb-3','style':'padding:3px'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(required=False,widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5,'style':'padding:3px'}))


    class Meta:
        model = Profile
        fields = ['avatar', 'bio']