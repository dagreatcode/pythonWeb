from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^home$', views.home, name='home'),
   url(r'^$', views.index, name='index'),
   url(r'^detail/$', views.detail, name='detail'),
   url(r'^add/$', views.add, name='add')
       # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
