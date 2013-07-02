from blog.views import PostList,SearchResults,ArchiveYear,ArchiveMonth
from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	#url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	url(r'^admin/', include(admin.site.urls), name='adminpage'),

	url(r'^$', RedirectView.as_view(url='/posts/')),
	url(r'^posts/', include('blog.urls')),
	url(r'^search/', SearchResults.as_view(), name='search'),
  	url(r'^contact/$', 'blog.views.contact',name='contact'),
  	url(r'^about/$', 'blog.views.about',name='about'),

	(r'^tinymce/', include('tinymce.urls')),
	
	url(r'^archive/$', 'blog.views.ArchiveYear', name='archiveyear'),
	url(r'^(?P<year>\d{4})/$', 'blog.views.ArchiveYear', name='archiveyear'),
	url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'blog.views.ArchiveMonth', name='archivemonth'),





#included in local app url ;)
##
#	url(r'^$', PostList.as_view(), name=u'mainpage'),
#	url(r'^posts/', PostList.as_view(), name=u'postlist'),
#	url(r'^/posts/(?P<slug>[a-zA-Z0-9_-]+)/$', PostDetails.as_view(), name='postdetails'),

)
