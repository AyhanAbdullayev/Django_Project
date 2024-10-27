from django import template

from Menu.models import Categories

register = template.Library()


register.simple_tag

def get_categories():
    category = Categories.objects.all()
    print(category,"----------")



