from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django_blog.sitemaps import BlogSitemap
from django.http import HttpResponse
from apps.blog import views

admin.autodiscover()

sitemaps = {
    'blog': BlogSitemap,
}

urlpatterns = [
        url(r'^about$', views.about, name='about'),
        # url(r'^blog/', include('apps.blog.urls', namespace='blog')),
        url(r'^', include('apps.blog.urls', namespace='blog')),
        url(r'^wedding/', include('apps.wedding.urls', namespace='wedding')),
        url(r'^admin/', include(admin.site.urls)),
        url(r'404', views.not_found),
        url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
           name='django.contrib.sitemaps.views.sitemap'),
        url(r'^robots.txt$',
           lambda r: HttpResponse("User-agent: *\nDisallow: /admin/\nSitemap: <http://simplecode.in/sitemap.xml>", content_type="text/plain")),
        url(r'^rss/', views.LatestPosts(), name='feeds')
      ]