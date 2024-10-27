from Menu.views import Menu
from django.urls import path




app_name = 'menu'


urlpatterns = [
    path("Menu/", Menu , name = "Menu_Page"),
]
