from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass

# đây là lớp trừu tượng
class BaseModel(models.Model):
    create_date = models.DateField(auto_now_add=True, null=True)
    update_date = models.DateField(auto_now_add=True, null=True)
    active = models.BooleanField(default=False)
    
    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Course(BaseModel):
    subject = models.CharField(max_length=255, null=False)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name