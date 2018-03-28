from django.contrib import admin

# Register your models here.

from .models import Hashtag, Post, User, Topic, Feed

#admin.site.register(Feed)
#admin.site.register(Post)
#admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Hashtag)

class PostInline(admin.TabularInline):
    model = Post
    extra = 0

@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ('daily_topic','next_topic')
    inlines = [PostInline]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('text','user','topic','post_date','post_time','upvote_count')
    fields = [('text','user','topic'),'upvote_count',('post_date','post_time')]

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email')
    inlines = [PostInline]

class TopicAdmin(admin.ModelAdmin):
    list_display = ('text','creator','active_date')
    inlines = [PostInline]
