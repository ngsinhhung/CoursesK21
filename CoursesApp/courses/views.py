
from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers

from .models import Course, Category, Lesson, User, Comment, Like
from .serializers import *
from .permissions import OwnerAuthenticated

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active = True).all()
    serializer_class = CourseSerializers

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(subject__icontains=q)

        cate_id = self.request.query_params.get('category_id')
        if cate_id:
            queries = queries.filter(category_id=cate_id)
        return queries
    @action(methods=['get'],detail=True)
    def lessons(self, request, pk):
        lessons = self.get_object().lesson_set.filter(active=True)
        return Response(serializers.LessonsSerializers(
            lessons, many=True, context={'request': request}).data, status = status.HTTP_200_OK)

class LessonViewSet(viewsets.ModelViewSet, generics.RetrieveAPIView):
    queryset = Lesson.objects.filter(active=True).all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.AllowAny()]

    def get_permissions(self):
        if self.action in ['add_comment', 'like']:
            return [permissions.IsAuthenticated()]
        return self.permission_classes

    @action(methods=['POST'], url_path="comments", detail=True)
    def add_comment(self,request,pk):
        c = Comment.objects.create(user=request.user, lesson = self.get_object(), content = request.data.get('content'))
        return Response(CommentSerializer(c).data, status = status.HTTP_201_CREATED)

    @action(methods=['POST'], url_path="like", detail=True)
    def like (self,request,pk):
        like, created = Like.objects.update_or_create(user = request.user, lesson = self.get_object())
        if not created:
            like.active = not like.active
            like.save()
        return Response(LessonDetailSerializer(self.get_object(), context={'request': request}).data,status = status.HTTP_201_CREATED)


class CommentViewSet(viewsets.ModelViewSet, generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [OwnerAuthenticated]

class UserViewSet(viewsets.ModelViewSet, generics.CreateAPIView):
    queryset =  User.objects.filter(is_active = True)
    serializer_class = UserSerializer