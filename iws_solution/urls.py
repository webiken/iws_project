from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'iws_solution.views.home', name='home'),
    url(r'^list(?:/(?P<client_id>\d+))?/$', 'iws_solution.views.list_features', name='list'),
    url(r'^edit/$', 'iws_solution.views.edit_feature', name='edit'),
    url(r'^admin/', include(admin.site.urls)),
]
