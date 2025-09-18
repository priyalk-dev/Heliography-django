from .models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    
    name = forms.CharField(required=True,
                           error_messages={'required':""},
                           widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Your Name"}))
    email = forms.EmailField(required=False,
                           error_messages={'required':""},
                           widget=forms.EmailInput(attrs={'class':'form-control','placeholder':"Enter Your Email"}))
    phone = forms.IntegerField(required=True,
                           error_messages={'required':""},
                           widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Your Phone"}))
    message = forms.CharField(required=True,
                           error_messages={'required':""},
                           widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Your Message"}))
    
    
    class Meta:
        model = Contact
        fields = ['name','email','phone','message']
        

