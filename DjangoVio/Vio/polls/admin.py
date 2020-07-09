from django.contrib import admin

from .models import Question,Choice

# class ChoiceInline(admin.TabularInline): 平层列表展示
class ChoiceInline(admin.StackedInline): # 顺序叠加展示
	model = Choice
	extra = 3 # 三个堆
class QuestionAdmin(admin.ModelAdmin):
	# 将默认的question_text顺序调整到后面
	# fields = ['pub_date','question_text']
	fieldsets = [
		(None,				{'fields':['question_text']}),
		('Date information',{'fields':['pub_date'],'classes':['collapse']}),
	]
	# 在新增页关联外键数据
	inlines = [ChoiceInline]
	# 把字段在admin页Question里打印出来
	list_display = ('question_text','pub_date','was_published_recently')
	# 增加一个过滤器的边栏，过滤值依据数据的属性
	list_filter = ['pub_date']
	# 增加搜索器
	search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)
# admin.site.register(Choice)
