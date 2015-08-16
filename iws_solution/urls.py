from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'iws_solution.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
