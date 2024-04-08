from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    #제목, 세부사항, 마감 기한
    title = models.CharField(max_length=100)
    content = models.TextField()
    deadline = models.DateTimeField(default=timezone.now)
    is_completed = models.BooleanField(default = False)
    
    def __str__(self):
        return self.title