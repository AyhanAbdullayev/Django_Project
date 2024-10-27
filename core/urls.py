from core.views import Home,About,Contact
from django.urls import path
from django.contrib import admin

app_name = 'core'

urlpatterns = [


    path("", Home , name = "Home_page"),

    path("Home/", Home , name = "Home_page"),

    path("About/", About , name = "About_page"),
    
    path("Contact/", Contact , name = "Contact_page" )
]
