from django.urls import path
from . import views
from django.conf.urls import url

app_name = "core"

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^detectWithWebcam', views.detectWithWebcam),
]