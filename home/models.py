from django.db import models

# Create your models here.
class BlogEntries(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    title = models.CharField(max_length=100)
    post = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

