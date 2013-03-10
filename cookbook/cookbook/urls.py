from django.conf.urls import patterns, include, url
import recipes.views
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'recipes.views.table_of_contents', name='home' ),
    url(r'^show_recipe', 'recipes.views.show_recipe'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^new_recipe', 'recipes.views.new_recipe'),
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    #        'document_root': settings.MEDIA_ROOT,}),
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
    #        'document_root': settings.STATIC_ROOT,}),
    #url(r'^enter_recipe$' , recipes.views.enter_recipe),
	#(r'^/recipe$' , recipes.views.show_recipe)
    # Examples:
    # url(r'^$', 'cookbook.views.home', name='home'),
    # url(r'^cookbook/', include('cookbook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()