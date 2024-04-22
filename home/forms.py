from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from home.models import ContactMessage, newsBlog,Events


class EventForm(forms.ModelForm):
    
    class Meta:
        model=Events
        fields = ('image','Description','name','Event_Start_Date','Event_End_Date')
        widgets={
            "Description":forms.Textarea(attrs={"rows":"4",'cols':'50','placeholder':"Enter Description"}),
             "name":forms.TextInput(attrs= {'placeholder':'Title'}),
             "Event_Start_Date": forms.DateInput(attrs={"type": "date"}),
            "Event_End_Date": forms.DateInput(attrs={"type": "date"}),
        }

class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message', 'subject']



class newsForm(forms.ModelForm):
    class Meta:
        model=newsBlog
        fields=('title','description','image')
        widgets={
            "title": forms.TextInput(attrs={'placeholder':'News Title'}),
            "description": forms.Textarea(attrs={"rows":"3","cols":"50",'placeholder':"Write News in Details..."}),
        }