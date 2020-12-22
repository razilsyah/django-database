from django.conf.urls import url

from . import views
urlpatterns = [
    # url blog home
    url(r'^$', views.index),

    # url blog category
    url(r'^(?P<categoryInput>[\w]+)/$', views.categoryPost),

    # url singpage
    url(r'^post/(?P<input>[\w-]+)/$', views.singlePage),

]
