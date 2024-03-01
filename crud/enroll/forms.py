from django import forms
from enroll.models import user
from django.core import validators
 

class registration(forms.ModelForm):
    class Meta:
        model = user
        fields = ['name', 'email', 'password']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        # password = cleaned_data('password')
        
        if len(name)<4:
            raise forms.ValidationError("Name should be greater than 4")
        elif len(name)>70:
            raise forms.ValidationError("Name should be smaller than 70")
        elif not name.isalnum():
            raise forms.ValidationError("Name Should be letter or number")
        
        return name 
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        # password = cleaned_data('password')
        
        if len(password)<4:
            raise forms.ValidationError("Password should be greater than 4")
        elif len(password)>70:
            raise forms.ValidationError("Password should be smaller than 70")
        
        
        return password 
    