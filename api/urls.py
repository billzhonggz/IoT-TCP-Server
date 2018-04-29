from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^location/*', views.query_location, name='location'),
    url(r'^status/*', views.query_alarm_status, name='alarm_status'),
]
