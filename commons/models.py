from django.db import models

# Create your models here.


class CommonModel(models.Model):

    """Common Model Definition"""

    """최초 생성 시간이 추가됨"""
    created_at = models.DateTimeField(auto_now_add=True)
    """데이터가 저장될 때마다 시간 업데이트"""
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
