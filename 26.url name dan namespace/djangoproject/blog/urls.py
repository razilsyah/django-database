from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^khusus/(?P<input>[\w-]+)$', views.Khusus, name='khusus'),
    url(r'^category/$', views.CategoryPost, name='category'),
    url(r'^single/$', views.SinglePost, name='single'),
    url(r'^$', views.index, name='index')
]
