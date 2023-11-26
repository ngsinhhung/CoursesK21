from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Course, Category, Tag

class TagSerializers(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name']

class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CourseSerializers(ModelSerializer):
    tags = TagSerializers(many=True)
    image = serializers.SerializerMethodField(source='image')
    class Meta:
        model = Course
        fields = ['id', 'subject', 'image', 'create_date', 'category', 'tags']


    def get_image(self, course):
        if(course.image):
            request = self.context.get('request')
            if(request):
                return request.build_absolute_uri('/static/%s' % course.image.name)
            return '/static/%s' % course.image.name
