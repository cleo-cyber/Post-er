from django.db import models

class Post(models.Model):
    created=models.DateTimeField(auto_now_add=True) #auto_now_add=True adds date automatically
    title=models.CharField(max_length=100 ,blank=False)
    content=models.TextField()
    author=models.CharField(max_length=100,blank=False)

    class Meta:
        ordering=['created'] #order blog posts based on date created 
