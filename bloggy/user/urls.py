from django.conf.urls import url

from .views import LoginView, logout_view

urlpatterns = [
    url(
        regex=r'login/$',
        view=LoginView.as_view(),
        name='login'
    ),
    url(
        regex=r'logout/$',
        view=logout_view,
        name='logout'
    )
]
