"""schoolweb URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('school.urls')),
    url(r'^docs/', include('rest_framework_docs.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)