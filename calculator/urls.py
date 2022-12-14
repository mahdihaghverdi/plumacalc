from django.urls import path

from calculator import views

urlpatterns = [
    path("", views.calculate, name="calculate"),
    path("<slug:postfix_para>", views.calculate, name="with_postfix"),
]
