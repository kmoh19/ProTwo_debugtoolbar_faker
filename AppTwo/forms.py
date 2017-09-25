from django import forms
from .models import User


class User_form(forms.ModelForm):
    class Meta:# or Meta() does not really matter?
        model=User
        fields= '__all__' # or if you are NOT interested in select fields -puth them in an iterable : exclude= ['field1','field2'] / to include use fields=['field1','field2']
        
        