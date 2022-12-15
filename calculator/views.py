import black
import postfixcalc
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import InputForm


def calculate(request: HttpRequest, postfix_para: str = "") -> HttpResponse:
    match request.method:
        case "GET":
            form = InputForm()
            return render(request, "calculator/index.html", {"form": form})

        case "POST":
            form = InputForm(request.POST)
            postfix, answer, errors = [None] * 3
            if form.is_valid():
                cd = form.cleaned_data["input"]
                try:
                    calc = postfixcalc.Calc(cd)
                    postfix = calc.postfix
                    answer = calc.answer
                except SyntaxError as e:
                    errors = e.msg
                except (TypeError, ValueError):
                    errors = "Wrong Input"
                return render(
                    request,
                    "calculator/index.html",
                    {
                        "form": form,
                        "input": cd,
                        "postfix": black.format_str(
                            mode=black.Mode(line_length=30),
                            src_contents=postfix.__str__(),
                        )
                        if postfix_para
                        else None,
                        "answer": answer,
                        "errors": errors,
                    },
                )


def calc_with_postfix(request: HttpRequest) -> HttpResponse:
    return calculate(request, 'something')
