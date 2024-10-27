from django.shortcuts import render
from .models import Meals,Categories


def Menu(request):
    Meal = Meals.objects.all()
    Categorie = Categories.objects.all()

    context = {
        'Meal': Meal,
        'Category':Categorie
    }

    return render(request,"Menu.html",context)
