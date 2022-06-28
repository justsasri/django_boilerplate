from django.urls import path

from . import views

urlpatterns = [
    path("", views.AppView.as_view(), name="app-index"),
    path("admin/", views.AdminView.as_view(), name="admin-index"),
]
