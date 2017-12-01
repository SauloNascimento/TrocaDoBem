from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.utils.text import slugify

from app.models import *

"""
admin.py: Definicao de classes para gerenciar no painel de admin do Django.
"""
__author__ = "Caio Marinho"
__copyright__ = "Copyright 2017, LES-UFCG"


class PostForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        exclude = ['slug']


class ImagePostAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'is_visible',)


class ImagePostInline(admin.TabularInline):
    model = ImagePost


class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name_item', 'owner', 'description', 'created_at')


class ObjectAdmin(admin.ModelAdmin):
    list_display = ('item', 'type', 'created_at')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('item', 'created_at')


class CommonUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')


class InstituteAdmin(admin.ModelAdmin):
    list_display = ('user', 'cnpj', 'created_at')


class RequirementAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'owner', 'created_at', 'status')


class PostAdmin(admin.ModelAdmin):
    inlines = [ImagePostInline, ]
    form = PostForm
    list_display = ('title', 'id', 'created_at', 'published_at', 'is_visible', 'author')
    ordering = ['-created_at']

    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        try:
            obj.slug = slugify(obj.title[:50])
        except:
            obj.slug = slugify(obj.title)
        super(PostAdmin, self).save_model(request, obj, form, change)


admin.site.register(Message, MessageAdmin)
admin.site.register(ImagePost, ImagePostAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Object, ObjectAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(CommonUser, CommonUserAdmin)
admin.site.register(Institute, InstituteAdmin)
admin.site.register(Requirement, RequirementAdmin)
