#!encoding=utf-8
from django.contrib.sites.models import Site
from django.contrib.sitemaps import Sitemap
from apps.blog.models import Blog


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    location = ""

    def get_urls(self, site=None, **kwargs):
        site = Site(domain='www.simplecode.in', name='www.simplecode.com')
        return super(BlogSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return Blog.objects.filter(is_public=True).filter(status='p')

    def lastmod(self, item):
        return item.add_time

    def location(self, item):
        return r'/blog/%d/%s' % (item.id, item.link)
