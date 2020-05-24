from django import forms
from django.contrib.auth.models import User
class SignupForm(forms.ModelForm):
    class Meta:
        model=User
        Fields=['Username','Password','Email','Firstname','Lastname']
