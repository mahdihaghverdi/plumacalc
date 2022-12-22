from django.urls import path

from calculator import views

urlpatterns = [
    path("", views.calculate, name="calculate"),
    path("history/", views.HistoryListView.as_view(), name="history"),
    path("heavy/", views.calc_heavy, name="heavy"),
]
