from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^home$', views.home, name='home'),
#    url(r'', views.index, name='index'),
#    url(r'^detail/$' views.detail, name='detail'),
   
]
