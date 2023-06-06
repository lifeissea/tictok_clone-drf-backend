from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        ("priofile",{
            "fields":(
            "avatar", "username", "password",  "email", "homepage", "bio",),
            "classes":("wide", "extrapretty"),
            }),
            )
    list_display = (
        "username",
        "email",
        'homepage',
        'bio',
        )
