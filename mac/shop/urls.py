from django.conf.urls import url
from .import views

urlpatterns=[
    url(r'^index/$',views.index),
    url(r'^about/$',views.about),
    url(r'^contact/$',views.contact),
    url(r'^tracker/$',views.tracker),
    url(r'^search/$',views.search),
    url(r'^products/<int:myid>/$',views.productview),
    url(r'^checkout/$',views.checkout),
]