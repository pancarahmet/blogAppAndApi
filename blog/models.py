from django.db import models
from django.contrib.auth.models import User


# Create your models here.




class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    resim=models.FileField(upload_to='blogPhoto',null=True,blank=True)
    

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    comment=models.TextField(max_length=400)
    created_at=models.DateTimeField(auto_now_add=True)
    blog=models.ForeignKey("Post",on_delete=models.CASCADE,related_name='comments')

    def __str__(self):
        return f"{self.author.username} - {self.blog.title}"
