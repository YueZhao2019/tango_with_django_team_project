from django.contrib import admin
from rango.models import Category, Page,Comment
from rango.models import UserProfile


# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'category', 'likes')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)


admin.site.register(Page, PageAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.register(UserProfile)