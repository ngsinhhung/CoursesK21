from django.contrib import admin
from .models import Category,Course,Tag,Lesson
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Course)
admin.site.register(Tag)
admin.site.register(Lesson)