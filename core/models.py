from django.db import models
from ckeditor.fields import RichTextField

class Comment(models.Model):
    Full_Name = models.CharField(max_length = 60)
    Email = models.EmailField(max_length = 200)
    City = models.CharField(max_length = 150)
    Message = RichTextField()

    def __str__(self):
        return self.Full_Name


