from django.contrib import admin

# Register your models here.

from .models import Hashtag, Post, Topic, Feed

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
    list_display = ('text','author','topic','upvote_count')
    fields = [('text','author','topic'),'upvote_count'] #post_date/time?

class TopicAdmin(admin.ModelAdmin):
    list_display = ('text','creator','active_date')
    inlines = [PostInline]
