from django.db import models

# Create your models here.
class task (models.Model):
    # slug = models.SlugField(unique=True)
    TaskTitle = models.CharField(max_length=50)
    # TaskInfo = models.TextField()
    # Date = models.DateTimeField(auto_now=True, auto_now_add=True)
    # DueDate = models.DateTimeField(auto_now=False, auto_now_add=False)