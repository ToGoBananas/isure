from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^ns/$', views.NSPView.as_view()),
    url(r'^ifl/$', views.IFLView.as_view()),
    url(r'^vzr/$', views.VZRView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)