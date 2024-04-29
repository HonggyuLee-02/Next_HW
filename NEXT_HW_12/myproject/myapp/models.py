from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    # last_visitor = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name="posts"
    # )
    # visited_at = models.DateField(auto_now = True)
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )

    def __str__(self):
        return self.content

class UserAccessLog(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='logs')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_accessed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} last accessed at {self.last_accessed}"