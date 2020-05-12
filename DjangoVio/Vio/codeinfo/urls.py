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
	path('results/delete', views.deleteid),
	path('delete/', views.codedelete, name='coderesult'),
	path('delete/confirm/', views.deleteconfirm,name='deleteconfirm'),
	path('delete/search/', views.codesearch, name='deletesearch'),
	path('update/',views.codemodify,name='codemodify'),
	path('update/<int:id>/',views.codemodifyid,name='codemodifyid'),
	path('update/confirm/',views.modifyconfirm,name='modifyconfirm')

]