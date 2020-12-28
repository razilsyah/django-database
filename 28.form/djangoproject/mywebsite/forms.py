from django import forms


class FormField(forms.Form):
    integer_field = forms.IntegerField()
