import black
import postfixcalc
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .forms import HeavyInputForm, InputForm
from .models import History


def calculate(
    request: HttpRequest,
    *,
    postfix_para: bool = False,
    heavy: bool = False,
) -> HttpResponse:
    history = History.objects.all().order_by("-created")[:5]
    match (request.method, heavy):
        case ("GET", False):
            form = InputForm()
            return render(
                request,
                "calculator/index.html",
                {"form": form, "history": history},
            )
        case ("GET", True):
            form = HeavyInputForm()
            return render(
                request,
                "calculator/index.html",
                {"form": form, "history": history},
            )

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
                except TimeoutError as e:
                    errors = e

                hist = History(input=cd, answer=answer, errors=errors)
                hist.save()

                history = History.objects.all().order_by("-created")[:5]
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
                        "history": history,
                    },
                )


def calc_with_postfix(request: HttpRequest) -> HttpResponse:
    return calculate(request, postfix_para=True)


def calc_heavy(request: HttpRequest) -> HttpResponse:
    return calculate(request, heavy=True)


class HistoryListView(ListView):
    template_name = "calculator/history.html"
    model = History
    context_object_name = "history"
    paginate_by = 15
