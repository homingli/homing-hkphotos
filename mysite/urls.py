from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns("",
    url(r"^$", direct_to_template, {"template": "homepage.html"}, name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^(?P<vendor>tn3)/$", direct_to_template, {"template": "homepage.html"}, name="home"),
    url(r"^(?P<vendor>galleria)/$", direct_to_template, {"template": "homepage.html"}, name="home"),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
