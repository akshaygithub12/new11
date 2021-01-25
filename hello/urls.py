from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("sections/<int:num>",views.section,name="section"),
    path("<str:name>",views.newname,name="newname"),
    path("akshay",views.akshay,name="aksahy"),
    path("vishal",views.vishal,name="vishal")
    ]
