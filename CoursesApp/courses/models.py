from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField




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
    description = RichTextField()
    image = models.ImageField(upload_to='courses/%Y/%m', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    tags = models.ManyToManyField('Tag')
    
    def __str__(self):
        return self.subject
    
    class Meta:
        unique_together = ('subject', 'category')


class Lesson(BaseModel):
    subject = models.CharField(max_length=255, null=False)
    content = RichTextField()
    image = models.ImageField(upload_to='lesson/%Y/%m', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='my_lesson')
    tags = models.ManyToManyField('Tag', blank=True, related_name='lessons')

    class Meta:
        unique_together = ('subject', 'course')


class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

