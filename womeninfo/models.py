from django.db import models

# Create your models here


class WomenModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/')
    cat=models.ForeignKey('Category',on_delete=models.PROTECT,null=True)

    def __str__(self):
        return self.title


class Category (models.Model):
    name = models.CharField(max_length=100, db_index=True)
    
    def __str__(self):
        return self.name