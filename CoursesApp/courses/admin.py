from django.contrib import admin
from django import forms
from django.db.models import Count
from django.template.response import TemplateResponse
from django.urls import path

from .models import Category, Course, Tag, Lesson
from django.utils.html import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.

class CourseAppAdminSite(admin.AdminSite):
    site_header = 'Hệ thống khóa học trực tuyến'

    def get_urls(self):
        return [
            path('course-stats/', self.stats_view)
        ] + super().get_urls()

    def stats_view(self,request):
        count = Course.objects.filter(active = True).count()
        stats = Course.objects\
            .annotate(lesson_count=Count('my_lesson'))\
            .values('id', 'subject', 'lesson_count')
        return TemplateResponse(request, 'admin.html', {
            'course_count': count,
            'course_stats': stats,
        })

admin_site = CourseAppAdminSite(name="myadmin")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]
    list_filter = ["id", "name"]

class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Course
        fields = '__all__'

class TabInlineAdmin(admin.StackedInline):
    model = Course.tags.through

class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ["img"]
    form = CourseForm
    inlines = [TabInlineAdmin]

    def img(self, Course):
        if Course:
            return mark_safe(
                '<img src="/static/{url}" width="120" />'.format(url=Course.image.name)
            )
    
    class Media:
        css = {
            'all': ('/static/style/style.css',)
        }




admin_site.register(Category, CategoryAdmin)
admin_site.register(Course, CourseAdmin)
admin_site.register(Tag)
admin_site.register(Lesson)
