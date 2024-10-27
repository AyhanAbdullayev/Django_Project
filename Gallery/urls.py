from Gallery.views import Gallery
from django.urls import path


app_name = 'Gallary'


urlpatterns = [
    path("Gallary/", Gallery , name = "Gallary_Page"),
]
