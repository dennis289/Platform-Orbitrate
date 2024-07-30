from django.contrib.sitemaps import Sitemap
from .models import Orbituaries

class ObituarySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Orbituaries.objects.all()

    def lastmod(self, obj):
        return obj.submission_date
