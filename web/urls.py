from django.conf.urls import url

from web.views import get_index, fetch

urlpatterns = [
    url(r'^$', get_index),
    url(r'^fetch/$', fetch),
]