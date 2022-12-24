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
                "placeholder": "Arithmatic expression",
            },
        ),
        help_text="<span class='form-text' style='font-family: monospace;'>e.g. (-1)^2 * 3</span>",
    )

    with_postfix = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )


class HeavyInputForm(InputForm):
    calculation_timeout = forms.ChoiceField(
        choices=[
            (0.5, "0.5"),
            (1, "1"),
            (1.5, "1.5"),
            (2, "2"),
            (2.5, "2.5"),
            (3, "3"),
            (4, "4"),
        ],
        widget=forms.Select(
            attrs={"class": "form-select form-select-sm"},
        ),
        label="Calculation Timeout (in seconds)",
    )

    str_representation_timeout = forms.ChoiceField(
        choices=[
            (5, "5"),
            (10, "10"),
            (15, "15"),
            (20, "20"),
        ],
        widget=forms.Select(
            attrs={"class": "form-select form-select-sm"},
        ),
        label="String Representation Timeout (in seconds)",
    )
