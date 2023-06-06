from django.db import models

from commons.models import CommonModel

# Create your models here.

class Video(CommonModel):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    file = models.URLField()
    thumbnail = models.URLField(blank=True)
    view_count = models.PositiveIntegerField(default=0, editable=False)
    like_count = models.PositiveIntegerField(default=0, editable=False)
    dislike_count = models.PositiveIntegerField(default=0, editable=False)
    comment_count = models.PositiveIntegerField(default=0, editable=False)
    comments = models.ManyToManyField("Comment", blank=True, related_name="videos")
    def __str__(self):
        return self.title
    
class Comment(CommonModel):
    message = models.TextField()
    creator = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, null=True, blank=True
    )
    video = models.ForeignKey(
        Video, on_delete=models.CASCADE, null=True, blank=True
    )
    def __str__(self):
        return self.message
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.video.comment_count = self.video.comments.count()
        self.video.save()
