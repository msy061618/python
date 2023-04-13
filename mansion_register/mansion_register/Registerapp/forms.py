from django import forms
from .models import Registerform


class DateInput(forms.DateInput):
    input_type = 'date'

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Registerform
        fields = '__all__'
        widgets = {
            'Date_Of_Joining': DateInput(),
        }  


 

