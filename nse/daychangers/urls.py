from django.conf.urls import url
from . import views
app_name = 'daychangers'

urlpatterns = [
	url(r'^$',views.login_user, name='login_user'),
    url(r'^index/$', views.index, name='index'),
    url(r'^register/$',views.register, name='register'),     
    url(r'^superindex/$',views.superindex, name='superindex'),
    url(r'^supergainer/$',views.supergainer, name='supergainer'),
    url(r'^superloser/$',views.superloser, name='superloser'), 
    url(r'^search$',views.search, name='search'),
    url(r'^result/$',views.result, name='result'),
    url(r'^stocklist/$',views.stocklist, name='stocklist'),
    url(r'^login/$',views.login_user, name='login_user'),

]
