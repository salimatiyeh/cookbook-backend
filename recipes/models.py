from django.db import models

class Recipe(models.Model):
        name = models.CharField(max_length=100)
        ingredients = models.TextField()
        instructions = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        cook_time = models.IntegerField(default=0)

def __str__(self):
    return self.name
