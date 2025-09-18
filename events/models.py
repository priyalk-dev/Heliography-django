from django.db import models

# Create your models here.
  
class Category(models.Model):
      name = models.CharField(max_length=100)
      
      def __str__(self):
          return self.name
  
  
class Events(models.Model):
      image = models.ImageField(upload_to='events/')
      category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='events',blank=True,null='True')
      
      def __str__(self):
          return f"Photo in {self.category.name}"
      