from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers
from .models import Course, Category
from .serializers import CourseSerializers, CategorySerializers


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
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