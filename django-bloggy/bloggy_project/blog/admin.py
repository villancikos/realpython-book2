from blog.models import Post
from django.contrib import admin

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'created_at','tag','image','views')

admin.site.register(Post, PostAdmin)
