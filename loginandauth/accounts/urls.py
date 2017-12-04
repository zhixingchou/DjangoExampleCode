from django.conf.urls import url, include
from accounts import user, permission

urlpatterns = [
    url(r'^login/$', user.login, name = 'login'),
    url(r'^user/list/$', user.user_list, name='user_list'),
    url(r'^user/add/$', user.user_add, name='user_add'),
    url(r'^user/delete/(?P<ids>\d+)/$', user.user_del, name='user_del'),
    url(r'^user/edit/(?P<ids>\d+)/$', user.user_edit, name='user_edit'),
    url(r'^reset/password/(?P<ids>\d+)/$', user.reset_password, name='reset_password'),
    # url(r'^role/list/$', role.role_list, name='role_list'),
    url(r'permission/deny/$', permission.permission_deny, name='permission_deny'),
]