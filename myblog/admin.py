from django.contrib import admin
from .models import Post, Postimg
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'pub_date',)


class ImgAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'imgname',)


admin.site.register(Post, PostAdmin)
admin.site.register(Postimg, ImgAdmin)
