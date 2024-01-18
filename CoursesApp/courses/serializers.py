from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Course, Category, Tag, Lesson, User, Comment

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
        fields = ['id', 'subject', 'image', 'created_date', 'updated_date', 'category', 'tags']


    def get_image(self, course):
        if(course.image):
            request = self.context.get('request')
            if(request):
                return request.build_absolute_uri('/static/%s' % course.image.name)
            return '/static/%s' % course.image.name

class LessonSerializer(ModelSerializer):
    tags = TagSerializers(many=True)
    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'image', 'tags', 'created_date', 'updated_date', 'content']

class LessonDetailSerializer(LessonSerializer):
    liked = serializers.SerializerMethodField()

    def get_liked(self, lesson):
        request = self.context.get('request')
        if request.user.is_authenticated:
            return lesson.like_set.filter(active=True).exists()
    class Meta:
        model = Lesson
        fields = LessonSerializer.Meta.fields + ['liked']

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'avatar_user']
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        data_user = validated_data.copy()
        user = User(**data_user)
        user.set_password(data_user['password'])
        user.save()
        return user

class CommentSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = ['id', 'content', 'user']