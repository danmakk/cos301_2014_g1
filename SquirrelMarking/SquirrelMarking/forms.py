from django import forms
import datetime

class LoginForm(forms.Form):
    username = forms.CharField(required=True)#pattern="u[0-9]{8}"
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
class AssessmentManagerForm(forms.Form):
    course = forms.CharField(required=True)
    assessmentName = forms.CharField(required=True)
    assessmentType = forms.CharField(required=True)
    markWeight = forms.CharField(required=True)   

class RenderForm(forms.Form):
    outputType = forms.CharField(required=True)# //type either csv or pdf
    assessment = forms.CharField(required=True) #// eg pracs, tests
    module = forms.CharField()#// eg COS212
    userID = forms.CharField()
    alteredTable = forms.CharField()
    dateFrom = forms.DateField(initial=datetime.date.today)
    dateTo = forms.DateField(initial=datetime.date.today)