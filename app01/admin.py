from django.contrib import admin

from app01.models import Author,Article

# Register your models here.

#后台的模型管理
class Articleadmin(admin.ModelAdmin):
    #设置要显示在列表中字段
    list_display = ('title', 'time', 'author')
    #搜索框
    search_fields = ('title', 'time',)
    #详细时间分别筛选
    date_hierarchy = 'time'
    #显示多对多关系
    filter_horizontal = ('classify',)
    #显示外键
    raw_id_fields = ('author',)

#注册数据库
admin.site.register(Article,Articleadmin)
admin.site.register(Author)