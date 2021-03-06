from django.conf.urls import *
from django.contrib import admin
##admin.autodiscover()
##from mysite.book import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       (r'^$', 'blog.views.index'),
                       url(
                           r'^blog/views/(?P<slug>[^\.]+).html',
                           'blog.views.view_post',
                           name='view_blog_post'),
                       url(
                           r'^blog/category/(?P<slug>[^\.]+).html',
                           'blog.views.view_category',
                           name='view_blog_category'),
##                       (r'^search-form/$', views.search_form),
##                       (r'^search/$', views.search),
##
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
