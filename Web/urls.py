from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path("admin/",admin.site.urls),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("",include("core.urls")),
    path("",include("Menu.urls")),
    path("",include("Gallery.urls")),
    path("",include("Blog.urls")),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_DIR)

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

