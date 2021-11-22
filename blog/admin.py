from django.contrib import admin

from .models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    list_display = ("title", "author", "body")


admin.site.register(Post, PostAdmin)
