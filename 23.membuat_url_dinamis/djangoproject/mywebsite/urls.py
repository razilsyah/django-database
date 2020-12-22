from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),

    # url(r'^angka/$', views.angka)
    url(r'^(?P<input>[0-9]{2})/$', views.angka),

    # tanggal
    url(r'^(?P<tahun>[0-9]{4})/(?P<tanggal>[0-9]{2})/(?P<hari>[0-9]{2})/$', views.tanggal),

    # slug
    url(r'^(?P<slug>[\w-]+)/$', views.link)


]
