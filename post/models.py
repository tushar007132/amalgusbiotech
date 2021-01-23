from django.db import models

# Create your models here.

class PostContent(models.Model):
    title=models.CharField(max_length=50)
    img=models.ImageField(upload_to='imges/')
    blogtext=models.TextField(max_length=500)
    date=models.DateField()

    def __str__(self):
        return self.title
