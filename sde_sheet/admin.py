from django.contrib import admin
from sde_sheet.models import *
# Register your models here.
class Filter(admin.ModelAdmin):
    list_filter = ("solved", "tags", "ds")

admin.site.register(DSA)
admin.site.register(Tag)
admin.site.register(Question, Filter,)
