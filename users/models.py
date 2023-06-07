from django.db import models
from django.contrib.auth.models import AbstractUser

from commons.models import CommonModel

# Create your models here.


class User(AbstractUser, CommonModel):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )
    email = models.EmailField(
        max_length=150,
        blank=True,
    )
    password = models.CharField(
        max_length=150,
        blank=True,
    )
    avatar = models.ImageField(blank=True)
    username = models.CharField(max_length=150, blank=True, unique=True)
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
        blank=True,
    )
    likes = models.PositiveIntegerField(
        default=0,
        editable=False,
    )
    homepage = models.URLField(
        blank=True,
    )
    bio = models.TextField(
        blank=True,
    )
    following = models.ManyToManyField(
        "self",
        through="UserFollow",
        through_fields=("follower", "following"),
        symmetrical=False,
        related_name="followers",
    )


class UserFollow(CommonModel):
    follower = models.ForeignKey(
        User, related_name="following_users", on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        User, related_name="follower_users", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (("follower", "following"),)
