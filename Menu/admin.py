from django.contrib import admin
from .models import Ratings,Categories,Calories,Types,Meals,Meal_Image
from django.utils.html import format_html


admin.site.register(Ratings)

admin.site.register(Categories)

admin.site.register(Calories)

admin.site.register(Meal_Image)

admin.site.register(Types)




class Meals_Images_Inline(admin.TabularInline):
    model = Meal_Image
    extra = 2



@admin.register(Meals)
class Meal_Admin(admin.ModelAdmin):
    list_display = ["id","Name","get_image","Categorie","Rating","Calories"]
    list_display_links = ["id","Categorie","Rating"]
    search_fields = ["Name"]
    inlines = [Meals_Images_Inline]


    fieldsets = (
        ("Food_info",{
            'fields':["Name","Count","Price","Image"]
        }),
        ("Relations",{
            "fields":["Rating","Categorie","Type","Calories"]
        })
    )


    def get_image(self,obj):
        if obj.Image:
            Image = f" <img src = '{obj.Image.url}'  width = '40'/> "

            return format_html(Image)
        
        return "No Image"
    get_image.short_description = "Image"



