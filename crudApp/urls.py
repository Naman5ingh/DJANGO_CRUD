from django.urls import path
from crudApp import views

urlpatterns = [
    path('',views.index, name="index"),
    path('about',views.about, name="about"),
    path('insert',views.insertData, name="insertData"),
    path('update/<id>',views.updateData, name="updateData"),
    path('delete/<id>',views.deleteData, name="updateData"),
    path('login',views.login_page, name="login_page"),
    path('register',views.register, name="register"),
    path('logout',views.logout_page, name="logout_page"),
]