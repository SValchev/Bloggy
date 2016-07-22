from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.list_posts, name='index'),
    url(r'(?P<id>\d+)/edit/$', views.edit_post,name='edit'),
    url(r'(?P<id>\d+)/delete/$', views.delete_post,name='delete'),
    url(r'add/$', views.add_post,name='add'),
    url(r'(?P<id>\d+)/$', views.info_post,name='info'),
]
