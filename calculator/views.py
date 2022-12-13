from django.http import HttpRequest, HttpResponse


def calculate(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello")
