from django import forms
from .models import Employee
from django.forms import widgets


class employeeform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'on_leave':widgets.HiddenInput(),
            'Leave_count':widgets.HiddenInput(),
        }