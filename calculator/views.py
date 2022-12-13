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
                try:
                    postfix = postfixcalc.infix_to_postfix(form.cleaned_data["input"])
                    answer = postfixcalc.evaluate(postfix)
                except SyntaxError as e:
                    errors = e
                return render(
                    request,
                    "calculator/index.html",
                    {
                        "form": form,
                        "postfix": postfix,
                        "answer": answer,
                        "errors": errors,
                    },
                )
