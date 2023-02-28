from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Sell,Comment
from django.forms import ModelForm

from .models import Profile


#Create forms here

class Sellform(ModelForm):
    class Meta:
        model = Sell
        fields = ['name', 'description', 'condition', 'price', 'category', 'brand','image']

class Commentform(ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


# Create a UserUpdateForm to update username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# Create a ProfileUpdateForm to update image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']



