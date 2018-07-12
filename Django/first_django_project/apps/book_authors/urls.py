from django.conf.urls import url
from . import views

#app_name = 'alpha_app'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^details$', views.details),
]