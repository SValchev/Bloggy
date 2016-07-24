from django.conf.urls import url

from .views import PostListView, PostDetailView, PostDeleteView, PostCreateView, PostCreateView
from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=PostListView.as_view(),
        name='index'
    ),
    url(
        regex=r'(?P<id>\d+)/edit/$',
        view=PostCreateView.as_view(),
        name='edit'
     ),
    url(
        regex=r'(?P<id>\d+)/delete/$',
        view=PostDeleteView.as_view(),
        name='delete'
    ),
    url(
        regex=r'add/$',
        view=PostCreateView.as_view(),
        name='add'
    ),
    url(
        regex=r'(?P<id>\d+)/$',
        view=PostDetailView.as_view(),
        name='info'
    ),
]
