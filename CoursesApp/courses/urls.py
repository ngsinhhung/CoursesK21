from django.urls import path, include
from  . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', views.CategoryViewSet, basename='category')
router.register('courses', views.CourseViewSet, basename= 'courses')
router.register('lesson', views.LessonViewSet, basename= 'lesson')
router.register('user', views.UserViewSet, basename= 'user')


urlpatterns = [
    path('', include(router.urls))
]