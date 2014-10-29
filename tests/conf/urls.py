from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^ftpdeploy/', include('ftp_deploy.urls')),
    url(r'^ftpdeploy/', include('ftp_deploy.server.urls')),
)
