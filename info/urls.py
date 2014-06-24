from django.conf.urls import patterns, include, url
from django.contrib import admin
from info import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'school.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', views.index, name='index'),
    url(r'^display/', views.display, name='display'),

)




