""" URL mappers to forward the supported URLs to view functions """
from django.urls import path
from . import views


app_name = "chill_check"


# URLConfiguration
urlpatterns = [
    # home page: home/
    path("home/", views.home, name="home"),
    # joy list: all
    path("all/", views.joy_list, name="joys"),
    # joy detail: detail/1
    path("detail/<int:joy_id>/", views.joy_detail, name="detail"),
    # joy edit: edit/1
    path("edit/<int:joy_id>/", views.joy_edit, name="edit"),
    # joy delete: delete/1
    path("delete/<int:joy_id>/", views.joy_delete, name="delete"),
    # user register: register/
    path("register/", views.user_register, name="register"),
    # user login: login/
    path("login/", views.user_login, name="login"),
    # user logout
    path("logout/", views.user_logout, name="logout")
]
