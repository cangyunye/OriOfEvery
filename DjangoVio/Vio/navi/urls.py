from django.urls import path

from . import views

app_name = 'navi'

urlpatterns = [
	path('',views.hi,name='hi'),
	path('msgb/',views.msgb,name='hi'),
	path('msgb/save/',views.msgsave,name='save'),
	path('wttr/',views.wttr,name='save')

]
