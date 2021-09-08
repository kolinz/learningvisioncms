from django.contrib import admin

# Register your models here.
from .models import Category, EduPost, Line, JobPost

class CategoryAdmin(admin.ModelAdmin):
  '''管理ページのレコード一覧に表示するカラムを設定するクラス
  
  '''
  # レコード一覧にidとtitleを表示
  list_display = ('id', 'title', 'summary')
  # 表示するカラムにリンクを設定
  list_display_links = ('id', 'title')

class EduPostAdmin(admin.ModelAdmin):
  '''管理ページのレコード一覧に表示するカラムを設定するクラス
  
  '''
  # レコード一覧にidとtitleを表示
  list_display = ('id', 'title', 'category', 'organizer')
  # 表示するカラムにリンクを設定
  list_display_links = ('id', 'title')

class LineAdmin(admin.ModelAdmin):
  '''管理ページのレコード一覧に表示するカラムを設定するクラス
  
  '''
  # レコード一覧にidとtitleを表示
  list_display = ('id', 'title', 'summary')
  # 表示するカラムにリンクを設定
  list_display_links = ('id', 'title', 'summary')

class JobPostAdmin(admin.ModelAdmin):
  '''管理ページのレコード一覧に表示するカラムを設定するクラス
  
  '''
  # レコード一覧にidとtitleを表示
  list_display = ('id', 'title')
  # 表示するカラムにリンクを設定
  list_display_links = ('id', 'title')


# Django管理サイトにCategory、CategoryAdminを登録する
admin.site.register(Category, CategoryAdmin)

# Django管理サイトにPhotoPost、PhotoPostAdminを登録する
admin.site.register(EduPost, EduPostAdmin)

# Django管理サイトにLine、LineAdminを登録する
admin.site.register(Line, LineAdmin)

# Django管理サイトにJobPost、JobPostAdminを登録する
admin.site.register(JobPost, JobPostAdmin)