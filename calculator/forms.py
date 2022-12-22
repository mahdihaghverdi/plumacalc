from django import forms
from django.forms import TextInput


class InputForm(forms.Form):
    input = forms.CharField(
        label="Expression",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "style": "font-family: monospace",
                "id": "userinput",
            },
        ),
    )

    with_postfix = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )


class HeavyInputForm(InputForm):
    heavy_calculations = forms.ChoiceField(
        choices=[(0.5, "0.5"), (1, "1"), (1.5, "1.5"), (2, "2")],
        widget=forms.Select(
            attrs={"class": "form-select form-select-sm"},
        ),
        label="Heavy calculations (in seconds)",
    )
