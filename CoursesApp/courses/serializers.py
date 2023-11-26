from rest_framework.serializers import ModelSerializer
from .models import Course, Category

class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CourseSerializers(ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'subject', 'create_date', 'category']