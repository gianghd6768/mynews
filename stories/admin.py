from django.contrib import admin
from stories.models import Story, Subcribe, Contact, Category

# Register your models here.
# from stories.models import Blog
#
class StoryAmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    list_filter = ('id',)

class CategoryAmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id',)

class ContactAmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_filter = ('id',)
# admin.site.register(Blog, blogAmin)

admin.site.register(Category, CategoryAmin)
admin.site.register(Story, StoryAmin)
admin.site.register(Contact, ContactAmin)
admin.site.register(Subcribe)

