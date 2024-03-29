from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  # Examples:
  # url(r'^$', 'mmcrp.views.home', name='home'),
  # url(r'^blog/', include('blog.urls')),

  url(r'^admin/', include(admin.site.urls)),
  url(r'^submit/', 'blog.views.submit', name='new'),
  url(r'^comments/', include('django.contrib.comments.urls')),
  url(r'^about/', 'blog.views.about', name='about'),
  url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'blog/login.html'}),
  url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}),
  url(r'^register/', 'blog.views.register', name='register'),
  url(r'^(?P<name>[\w\-]+)/$', 'blog.views.post'),
  url(r'^(?P<name>[\w|\W]+)/$', 'blog.views.post'),
  url(r'^$', 'blog.views.index', name='home1'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
