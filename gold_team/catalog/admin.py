from django.contrib import admin

# Register your models here.

from .models import Hashtag, Post, User, Topic, Feed

admin.site.register(Hashtag)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Feed)