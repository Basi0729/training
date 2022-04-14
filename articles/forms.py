
from django import forms
from django.forms import ModelForm
from articles.models import Profile

class NewProfile(ModelForm):
    class Meta:
        model=Profile
        fields=('name',"age","occupation",'place',
        'joining_date','email_id','profile_Main_Img')
        