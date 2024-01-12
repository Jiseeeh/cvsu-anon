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
    path("dashboard/sent_messages/", views.sent_messages, name="sent_messages"),
    path("homepage/", views.homepage, name="homepage"),
    path("get_messages_sent/", views.get_messages_sent, name="get_messages_sent"),
    path("patch_message/<int:message_id>/",
         views.patch_message, name="patch_message")
]
