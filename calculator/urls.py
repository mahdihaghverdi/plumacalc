from django.urls import path

from calculator import views

urlpatterns = [
    path("", views.calculate, name="calculate"),
    path("postfix/", views.calc_with_postfix, name="with_postfix"),
    path("history/", views.HistoryListView.as_view(), name="history"),
]
