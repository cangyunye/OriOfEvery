from django.urls import path
from . import views
urlpatterns = [
	path('', views.index, name='codeindex'),
	path('speresult/',views.codesperesult,name='codesperesult'),
	path('load/',views.codeload,name='codeload'),
	path('load/save/', views.codespesave, name='codespesave'),
	path('search/', views.codesearch, name='codesearch'),
	path('add/', views.codeadd, name='codeadd'),
	path('add/save/', views.codesave, name='codesave'),
	path('results/', views.coderesults, name='coderesult'),
	path('delete/', views.codedelete, name='coderesult'),
	path('delete/search/', views.codedelete, name='coderesult'),

]