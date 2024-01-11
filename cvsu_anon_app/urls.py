from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("send/u/<str:username>/", views.send_anon, name="send_anon_message"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/delete/<int:message_id>/",
         views.delete_message, name="delete_message"),
    path("homepage/", views.homepage, name="homepage"),
]
