from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^ns/$', views.NSPView.as_view()),
    url(r'^ifl/$', views.IFLView.as_view()),
    url(r'^vzr/$', views.VZRView.as_view()),
    url(r'^accidents/$', views.InsuredAccidentView.as_view()),
    url(r'^changes/$', views.RequestChangesView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)