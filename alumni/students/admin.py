from django.contrib import admin
from students import models
from django.contrib.admin.options import ModelAdmin
class NoticeAdmin(ModelAdmin):
    list_display = ["subject", "cr_date"]
    search_fields = ["subject", "msg"]
    list_filter = ["cr_date"]
#admin.site.register(models.Notice)
admin.site.register(models.Notice, NoticeAdmin)


# Register your models here.
