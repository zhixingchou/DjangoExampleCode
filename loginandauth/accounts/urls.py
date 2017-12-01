from django.conf.urls import url, include
from accounts import user

urlpatterns = [
    url(r'^login/$', user.login, name = 'login'),
]