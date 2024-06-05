from django.contrib import admin
from .models import *
from .forms import *


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


admin.site.register(UserInfo)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Rate)
