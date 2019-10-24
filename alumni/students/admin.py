from django.contrib import admin
from . models import Notice, Albums,Branch , Profile, FollowUser, MyPost, PostComment, PostLike
from django.contrib.admin.options import ModelAdmin
from . import models
class NoticeAdmin(ModelAdmin):
    list_display = ["subject", "cr_date"]
    search_fields = ["subject", "msg"]
    list_filter = ["cr_date"]
admin.site.register(Notice, NoticeAdmin)

class AlbumsAdmin(ModelAdmin):
    list_display = ["meetupplace","image"]
    search_fields = ["meetupplace"]
    list_filter = ["meetupplace"]
admin.site.register(Albums,AlbumsAdmin)

admin.site.register(models.pictures)
#admin.site.register(models.Notice)

# admin.site.register(models.Memories)
class BranchAdmin(ModelAdmin):
    list_display = ["name", "hod"]
    search_fields = ["name"]
    list_filter = ["name","batch"]
admin.site.register(Branch, BranchAdmin)

class ProfileAdmin(ModelAdmin):
    list_display= ["name"]
    search_fields = ["name","status","phone_no"]
    list_filter = ["status","gender"]
admin.site.register(Profile, ProfileAdmin)

class FollowUserAdmin(ModelAdmin):
    list_display= ["profile","followed_by"]
    search_fields = ["profile","followed_by"]
    list_filter =  ["profile","followed_by"]
admin.site.register(FollowUser, FollowUserAdmin)

class MyPostAdmin(ModelAdmin):
    list_display= ["subject","cr_date","uploaded_by"]
    search_fields = ["subject","msg","uploaded_by"]
    list_filter = ["cr_date","uploaded_by"]
admin.site.register(MyPost, MyPostAdmin)

class PostCommentAdmin(ModelAdmin):
    list_display= ["post","msg"]
    search_fields = ["msg","post","commented_by"]
    list_filter = ["cr_date","flag"]
admin.site.register(PostComment, PostCommentAdmin)

class PostLikeAdmin(ModelAdmin):
    list_display= ["post","liked_by"]
    search_fields = ["post","liked_by"]
    list_filter = ["cr_date"]
admin.site.register(PostLike, PostLikeAdmin)
# Register your models here.
