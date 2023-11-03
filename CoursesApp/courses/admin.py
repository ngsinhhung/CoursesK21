from django.contrib import admin
from django.forms.widgets import Media
from django import forms
from .models import Category, Course, Tag, Lesson
from django.utils.html import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.


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




admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Tag)
admin.site.register(Lesson)
