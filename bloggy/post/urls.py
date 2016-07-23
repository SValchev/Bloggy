from django.conf.urls import url

from .views import CustomListView
from . import views

urlpatterns = [
    url(r'^$', CustomListView.as_view(), name='index'),
    url(r'(?P<id>\d+)/edit/$', views.edit_post,name='edit'),
    url(r'(?P<id>\d+)/delete/$', views.delete_post,name='delete'),
    url(r'add/$', views.add_post,name='add'),
    url(r'(?P<id>\d+)/$', views.info_post,name='info'),
]
