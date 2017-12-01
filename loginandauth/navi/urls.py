from django.conf.urls import url, include
from navi import views

urlpatterns = [
    url(r'^$', views.index, name='navi'),
]



