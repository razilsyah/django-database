from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index, name='index'),
    url(r'post/(?P<slugInput>[\w-]+)$', views.DetailPost, name='detail'),
    url(r'category/(?P<categoryInput>[\w-]+)$',
        views.CategoryPost, name='category')
]
