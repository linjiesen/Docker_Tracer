# from django.urls import re_path
from django.conf.urls import url
from SMS import views

urlpatterns = [
    url(r'^send/sms/', views.send_sms),
    url(r'^register/', views.register, name='register'),
]
