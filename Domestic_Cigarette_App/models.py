from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.
class Domestic_Cigarette_Category(models.Model) :
  Category = models.CharField(max_length=100)
  
  def __str__(self) :
    return self.Category
    
    
class Domestic_Cigarette(models.Model) :
  Category = models.CharField(max_length=100)
  Name = models.CharField(max_length=100)
  Price = models.IntegerField(default=0)
  Tar = models.DecimalField(default=0, max_digits=2, decimal_places=1)
  Nicotine = models.DecimalField(default=0, max_digits=3, decimal_places=2)
  StarPoints = models.PositiveIntegerField(default=0)
  StarPoint = models.DecimalField(default=0, max_digits=2, decimal_places=1)
  
  def __str__(self) :
    return self.Name
    
  def get_absolute_url(self) :
    return reverse('Domestic_Cigarette_App:RCD', args=[self.Name])
    
  def StarPointUpdate(self, StarPoint) :
    self.StarPoints += StarPoint
    self.StarPoint = self.StarPoints / self.Comments.count()
    self.save()
  
  def StarPointDelete(self, StarPoint) :
    self.StarPoints -= StarPoint
    if(self.Comments.count() - 1 <= 0) :
      self.StarPoint = 0
    else :
      self.StarPoint = self.StarPoints / (self.Comments.count() - 1)
    self.save() 
    
    
class Domestic_Cigarette_Comment(models.Model) :
  Object = models.ForeignKey(Domestic_Cigarette, on_delete=models.CASCADE, related_name='Comments')
  Nickname = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='D_Nickname')
  Content = models.CharField(max_length=100)
  StarPoint = models.PositiveSmallIntegerField(default=0)
  
  def __str__(self) :
    return self.Nickname.username
    
