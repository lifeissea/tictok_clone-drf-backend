from django.contrib import admin

from videos.models import Video

# Register your models here.
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    fieldsets = (
        ("priofile",{
            "fields":(
            "title", "description", "file", "thumbnail",),
            "classes":("wide", "extrapretty"),
            }),
            )
    
    list_display = (
        "title",
        "description",
        "file",
        "thumbnail",
        "view_count",
        "like_count",
        "comment_count",
        "created_at",
        "updated_at",
    )