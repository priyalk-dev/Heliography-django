from django.db import models

# Create your models here.
class Contact(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField(max_length=10,null=False,blank=False,default="0000000000")
    message=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
