from django.conf.urls import url
from .import views

urlpatterns=[
    url('index',views.index , name='blogHome'),
    url('blogpost/(?P<id>\d+)/',views.blogpost , name= 'blogpost'),
]