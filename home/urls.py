from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('login/', login_view, name="login_view"),
    path('register/', register_view, name="register_view"),
    path('add-Blog/', add_Blog, name="add_Blog"),
    path('Blog-detail/<slug>', Blog_detail, name="Blog_detail"),
    path('see-Blog/', see_Blog, name="see_Blog"),
    path('Blog-delete/<id>', Blog_delete, name="Blog_delete"),
    path('Blog-update/<slug>/', Blog_update, name="Blog_update"),
    path('logout-view/', logout_view, name="logout_view"),
    path('verify/<token>/', verify, name="verify")
]