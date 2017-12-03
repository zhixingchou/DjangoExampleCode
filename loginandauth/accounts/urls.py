from django.conf.urls import url, include
from accounts import user, permission

urlpatterns = [
    url(r'^login/$', user.login, name = 'login'),
    url(r'permission/deny/$', permission.permission_deny, name='permission_deny'),
]