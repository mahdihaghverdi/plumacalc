import black
import postfixcalc
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .forms import InputForm
from .models import History


def calculate(request: HttpRequest, postfix_para: str = "") -> HttpResponse:
    history = History.objects.all().order_by('-created')[:5]
    match request.method:
        case "GET":
            form = InputForm()
            return render(request, "calculator/index.html", {"form": form, 'history': history})

        case "POST":
            form = InputForm(request.POST)
            postfix, answer, errors = [None] * 3
            if form.is_valid():
                cd = form.cleaned_data["input"]
                try:
                    calc = postfixcalc.Calc(cd)
                    postfix = calc.postfix
                    answer = calc.answer
                    hist = History(input=cd, answer=answer)
                    hist.save()
                except SyntaxError as e:
                    errors = e.msg
                except (TypeError, ValueError):
                    errors = "Wrong Input"

                history = History.objects.all().order_by('-created')[:5]
                return render(
                    request,
                    "calculator/index.html",
                    {
                        "form": form,
                        "input": cd,
                        "postfix": black.format_str(
                            mode=black.Mode(line_length=20),
                            src_contents=postfix.__str__(),
                        )
                        if postfix_para
                        else None,
                        "answer": answer,
                        "errors": errors,
                        'history': history
                    },
                )


def calc_with_postfix(request: HttpRequest) -> HttpResponse:
    return calculate(request, 'something')


class HistoryListView(ListView):
    template_name = 'calculator/history.html'
    model = History
    context_object_name = 'history'
    paginate_by = 10
