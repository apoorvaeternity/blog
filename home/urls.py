from django.conf.urls import url,include

from . import views

app_name = 'home'
urlpatterns = [
    url(r'^blogs/$', views.blog_view, name='blog_page'),
]
