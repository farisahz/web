from django import forms
#from django.contrib.auth import forms
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import adminuser
from django.forms import ModelForm

class SignUpForm(forms.ModelForm):
   email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
   #no_phone = forms.CharField(max_length=12)
   password = forms.CharField(widget=forms.PasswordInput())
   password2 = forms.CharField(widget=forms.PasswordInput())
   
   class Meta:
        model = adminuser
        fields = ['username', 'email', 'no_phone', 'password', 'password2']

   def clean(self):
      cleaned_data = super(SignUpForm, self).clean()
      
      password = cleaned_data.get('password')
      password2 = cleaned_data.get('password2')
      
      if password and password2:
         if password != password2:
            raise forms.ValidationError("The two password fields must match.")
            
      return cleaned_data
   
   def save(self, commit=True):
      user=super(adminuser, self).save(commit=False)
      user.email = self.cleaned_data["email"]
      if commit:
         user.save()
      return user

class ProfileForm(ModelForm):
         class Meta:
            model = adminuser
            fields = ('username','email','no_phone')