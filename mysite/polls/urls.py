from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
