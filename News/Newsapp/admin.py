from django.contrib import admin
from Newsapp import models
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display=('id','catego','fakename','title','message','pubtime','enable','press')
    list_filter=('catego','press','fakename')
    search_fields=('catego','title')
    ordering=('id')

admin.site.register(models.NewsTable)