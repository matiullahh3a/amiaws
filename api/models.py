from django.db import models

# Create your models here.
class Profile(models.Model):
  name = models.CharField(max_length=70, null=True, blank=True)
  test=models.CharField(max_length=20,null=True, blank=True)
  enroll =models.IntegerField(null=True, blank=True)
  email_id = models.EmailField(null=True, blank=True )
  phone_number = models.CharField(max_length=12, unique=True,null=True)



  def __str__(self):
    return self.test






