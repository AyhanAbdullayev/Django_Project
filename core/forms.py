from django import forms
from core.models import Comment
from django.core.exceptions import ValidationError

class FormComment(forms.ModelForm):
    
    class Meta:
        model = Comment 
        fields = ("Full_Name","Email","City","Message")

        widgets = {
            "Full_Name" : forms.TextInput(attrs = {
                "class" : "form-control",
                "placeholder": "Enter your Full Name",
            }),
            "Email": forms.EmailInput(attrs = {
                "class" : "form-control",
                "placeholder": "Enter your Email",
                "aria-describedby": "validationTooltipUsernamePrepend",
            }),
            "City" : forms.TextInput(attrs = {
                "class": "form-control",
                "placeholder": "Enter your City",
            }),
            "Message" : forms.TextInput(attrs = {
                "class" : "form-control",
                "placeholder": " Enter Message",
            }),
        }

    

    def clean(self):
        cleaned_data = self.cleaned_data

        if self.data["Full_Name"] == 'Adolf Hitler':
            raise forms.ValidationError("Your Full Name can't be Adolf Hitler.")
        else:
            return cleaned_data



    def clean_Email(self):
        value = self.cleaned_data.get("Email")

        if not value.endswith(".com"):
            raise forms.ValidationError("This email isn't correct or not supported.")
        
        return value


        
