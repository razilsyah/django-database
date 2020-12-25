from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index),
    url(r'post/(?P<slugInput>[\w-]+)$', views.DetailPost),
    url(r'category/(?P<categoryInput>[\w-]+)$', views.CategoryPost)
]
