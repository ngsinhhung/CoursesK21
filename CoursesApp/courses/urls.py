from django.urls import path, include
from  . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', views.CategoryViewSet, basename='category')
router.register('courses', views.CourseViewSet, basename= 'courses')
router.register('lessons', views.LessonViewSet, basename= 'lessons')
router.register('users', views.UserViewSet, basename= 'users')
router.register('comments', views.CommentViewSet, basename= 'comments')



urlpatterns = [
    path('', include(router.urls))
]