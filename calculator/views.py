import black
import postfixcalc
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .forms import HeavyInputForm, InputForm
from .models import History


def calculate(request: HttpRequest, *, heavy: bool = False) -> HttpResponse:
    history = History.objects.all().order_by("-created")[:5]
    match request.method:
        case "GET":
            form = InputForm() if not heavy else HeavyInputForm()
            return render(
                request,
                "calculator/index.html",
                context={"form": form, "history": history},
            )

        case "POST":
            form = (
                InputForm(request.POST) if not heavy else HeavyInputForm(request.POST)
            )
            postfix, answer, errors = [None] * 3
            print(form.is_valid())

            if form.is_valid():
                input_ = form.cleaned_data["input"]
                with_postfix = form.cleaned_data["with_postfix"]
                try:
                    if heavy:
                        timeout = form.cleaned_data["heavy_calculations"]
                        calc = postfixcalc.Calc(input_, timeout=float(timeout))
                    else:
                        calc = postfixcalc.Calc(input_)
                    postfix = calc.postfix
                    answer = calc.stranswer
                except SyntaxError as e:
                    errors = e.msg
                except (TypeError, ValueError) as e:
                    if isinstance(e, ValueError) and "took" in e.__str__():
                        errors = e.__str__()
                    else:
                        errors = f"Wrong Input: {input_!r}"
                except TimeoutError as e:
                    errors = e.__str__()

                hist = History(input=input_, answer=answer, errors=errors)
                hist.save()

                history = History.objects.all().order_by("-created")[:5]
                return render(
                    request,
                    "calculator/index.html",
                    {
                        "form": form,
                        "input": input_,
                        "postfix": black.format_str(
                            mode=black.Mode(line_length=30),
                            src_contents=postfix.__str__(),
                        )
                        if with_postfix
                        else None,
                        "answer": answer,
                        "errors": errors,
                        "history": history,
                    },
                )


def calc_heavy(request: HttpRequest) -> HttpResponse:
    return calculate(request, heavy=True)


class HistoryListView(ListView):
    template_name = "calculator/history.html"
    model = History
    context_object_name = "history"
    paginate_by = 15
