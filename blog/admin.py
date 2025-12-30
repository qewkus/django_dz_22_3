from django.contrib import admin
from blog.models import Post
# Register your models here.

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title", )
