from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from school.api import views
from school.views import api_root

urlpatterns = [
    url(r'^$', api_root),
    url(r'^schools/$', views.SchoolList.as_view(), name="school-list"),
    url(r'^schools/(?P<pk>[0-9]+)/$', views.SchoolDetail.as_view(), name="school-detail"),
    url(r'^students/$', views.StudentList.as_view(), name="student-list"),
    url(r'^students/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view(), name="student-detail"), 
]
urlpatterns = format_suffix_patterns(urlpatterns)