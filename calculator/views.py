import postfixcalc
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import InputForm


def calculate(request: HttpRequest) -> HttpResponse:
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
                    postfix = postfixcalc.infix_to_postfix(cd)
                    answer = postfixcalc.evaluate(cd)
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
                        "postfix": postfix,
                        "answer": answer,
                        "errors": errors,
                    },
                )
