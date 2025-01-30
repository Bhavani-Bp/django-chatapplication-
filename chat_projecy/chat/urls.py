from django.urls import path
from .views import  login_view, home_view, chat_room_view,register_view

urlpatterns = [

    path("login/", login_view, name="login"),
    path("", home_view, name="home"),  # Home page
    path("register/", register_view, name="register"),
    path("chat/<str:room_name>/", chat_room_view, name="chat_room"),  # Chat room
]
