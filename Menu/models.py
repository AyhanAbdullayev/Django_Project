from django.db import models


class Ratings(models.Model):
    Rating = models.FloatField(null = True)

    def __str__(self):
        return f"{self.Rating}"

    class Meta:
        verbose_name_plural = "Ratings"
        verbose_name = "Rating"


    

class Categories(models.Model):
    Category = models.CharField(max_length = 190,null = True)
    Image = models.ImageField(upload_to = "Images/")

    def __str__(self):
        return self.Category
    
    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"


class Datetime(models.Model):
    Created_at = models.DateTimeField(auto_now_add = True)
    Updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True


class Calories(models.Model):
    Calory = models.IntegerField(null = True)

    def __str__(self):
        return f"{self.Calory}"
    
    class Meta:
        verbose_name_plural = "Calories"
        verbose_name = "Calory"


class Types(models.Model):
    Type = models.CharField(max_length = 180, null = True)

    def __str__(self):
        return self.Type
    
    class Meta:
        verbose_name_plural = "Types"
        verbose_name = "Type"


class Meals(Datetime):
    Name = models.CharField(max_length = 200)
    Rating = models.ForeignKey(Ratings,on_delete = models.SET_NULL, null = True)
    Type = models.ForeignKey(Types,on_delete = models.SET_NULL,null = True)
    Categorie = models.ForeignKey(Categories, on_delete = models.SET_NULL , null = True)
    Calories = models.ForeignKey(Calories,on_delete = models.SET_NULL , null = True)
    Count = models.IntegerField()
    Price = models.IntegerField()
    Image  =  models.ImageField(upload_to = "Images/")

    def __str__(self):
        return f"{self.Name} "
    

    class Meta:
        verbose_name_plural = "Meals"
        verbose_name = "Meal"
        ordering = ["Created_at"]




class Meal_Image(Datetime):
    Image = models.ImageField(upload_to = 'Images/',null = True,blank = True)
    Meal = models.ForeignKey("Meals", on_delete = models.CASCADE, related_name = "image",null = True,blank = True)

    def __str__(self):
        return f"{self.Meal.Name}"
    
    class Meta:
        verbose_name_plural = "Meal_Images"
        verbose_name = "Meal_Image"



