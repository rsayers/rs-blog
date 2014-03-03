from django.contrib import admin
from blogapp.models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['title','created']
    # fields to filter the change list with
    list_filter = ['published', 'created']
    # fields to search in change list
    search_fields = ['title', 'content']
    # enable the date drill down on change list
    date_hierarchy = 'created'
    # enable the save buttons on top on change form
    save_on_top = True
    # prepopulate the slug from the title - big timesaver!

    
admin.site.register(Post, PostAdmin)
