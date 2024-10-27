from django.contrib import admin


from .models import Comment



@admin.register(Comment)

class  Show_fields(admin.ModelAdmin):
    list_display = ["Full_Name","Email","City"]
