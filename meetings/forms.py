
from django import forms

class CalendarForm(forms.Form):
    cal_field = forms.DateTimeField()