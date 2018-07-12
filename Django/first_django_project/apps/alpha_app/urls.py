from django.conf.urls import url
from . import views

#app_name = 'alpha_app'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^test$', views.test),
    url(r'^(?P<slug>[\w-]+)/$',views.article_details, name = 'details'),
]