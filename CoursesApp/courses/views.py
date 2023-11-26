from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Course, Category
from .serializers import CourseSerializers, CategorySerializers


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active = True)
    serializer_class = CourseSerializers

