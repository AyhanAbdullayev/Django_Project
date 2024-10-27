from Blog.views import Blog
from django.urls import path
from django.contrib import admin


app_name = "Blog"


urlpatterns = [
    path("Blog/", Blog , name =  "Blog_Page")
]
