from django.db import models

# Create your models here.
class task (models.Model):
    
    TaskTitle = models.CharField(max_length=50)
    TaskInfo = models.TextField()
    Date = models.DateTimeField(auto_now_add=True, blank=True)
    DueDate = models.DateTimeField(null=True ,auto_now_add=False, blank=False)