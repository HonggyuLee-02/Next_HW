from django.db import models
from django.utils import timezone

# 현재 시간(서울 시간대 기준) 가져오기
now_seoul = timezone.localtime(timezone.now())

# Create your models here.
class Hobby(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Food(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Programming(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


#댓글 기능 추가
class Hobby_Comment(models.Model):
    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE, related_name = 'comments')
    writer = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.writer) + timezone.localtime(self.created_at).strftime('%Y-%m-%d-%H-%M-%S')
class Food_Comment(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="comments")
    writer = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.writer) + timezone.localtime(self.created_at).strftime('%Y-%m-%d-%H-%M-%S')

class Programming_Comment(models.Model):
    Programming = models.ForeignKey(Programming, on_delete=models.CASCADE, related_name="comments")
    writer = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.writer) + timezone.localtime(self.created_at).strftime('%Y-%m-%d-%H-%M-%S')
    
    
#대댓글 기능
class Hobby_cocoment(models.Model):
    parent = models.ForeignKey(Hobby_Comment,on_delete=models.CASCADE, related_name='cocoments')
    writer = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.writer) + timezone.localtime(self.created_at).strftime('%Y-%m-%d-%H-%M-%S')
class Food_cocoment(models.Model):
    parent = models.ForeignKey(Food_Comment,on_delete=models.CASCADE, related_name='cocoments')
    writer = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.writer) + timezone.localtime(self.created_at).strftime('%Y-%m-%d-%H-%M-%S')
class Programming_cocoment(models.Model):
    parent = models.ForeignKey(Programming_Comment,on_delete=models.CASCADE, related_name='cocoments')
    writer = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.writer) + timezone.localtime(self.created_at).strftime('%Y-%m-%d-%H-%M-%S')