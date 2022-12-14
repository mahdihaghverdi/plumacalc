from django import forms
from django.forms import TextInput


class InputForm(forms.Form):
    input = forms.CharField(
        label="Expression",
        label_suffix=": ",
        empty_value="Arithmetic Expression",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "style": "font-family: monospace",
                "id": "userinput",
            },
        ),
    )
