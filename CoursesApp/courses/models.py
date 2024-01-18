from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField



# Create your models here.
class User(AbstractUser):
    avatar_user = CloudinaryField('avatar', null = True)


# đây là lớp trừu tượng
class BaseModel(models.Model):
    created_date = models.DateField(auto_now_add=True, null=True)
    updated_date = models.DateField(auto_now_add=True, null=True)
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

    def __str__(self):
        return self.subject

    class Meta:
        unique_together = ('subject', 'course')


class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
class Interaction(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = False)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=False)
    class Meta:
        abstract = True

class Comment(Interaction):
    content = models.CharField(max_length=255, null = True)

class Like(Interaction):
    active = models.BooleanField(default = True);
    class Meta:
        unique_together = ['user', 'lesson']

class Rating(Interaction):
    rating = models.SmallIntegerField(default=0)