from django.conf.urls import re_path
from core import views

app_name = 'core'
urlpatterns = [
	re_path(r'^$',views.login,name='login'),
	re_path(r'^home/$',views.home,name='home'),
	re_path(r'^planner/$',views.planner,name='planner'),

	re_path(r'^patient/$',views.PatientList.as_view(),name='patient_index'),
	re_path(r'^patient/create/$',views.PatientCreate.as_view(),name='patient_create'),
	re_path(r'^patient/(?P<pk>[0-9]+)/$',views.PatientDetail.as_view(),name='patient_detail'),
	re_path(r'^patient/(?P<pk>[0-9]+)/update/$',views.PatientUpdate.as_view(),name='patient_update'),
	re_path(r'^patient/(?P<pk>[0-9]+)/remove/$',views.PatientDelete.as_view(),name='patient_delete'),

	re_path(r'^form/$',views.FormList.as_view(),name='form_index'),
	re_path(r'^form/create/$',views.FormCreate.as_view(),name='form_create'),
	re_path(r'^form/(?P<pk>[0-9]+)/view/$',views.FormView.as_view(),name='form_view'),
	re_path(r'^form/(?P<pk>[0-9]+)/edit/$',views.FormUpdate.as_view(),name='form_update'),
	re_path(r'^form/(?P<pk>[0-9]+)/remove/$',views.FormDelete.as_view(),name='form_delete'),
]

