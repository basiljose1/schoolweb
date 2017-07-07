# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

#view to list all the api with hyperlink
@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'schools': reverse('school-list', request=request, format=format),
        'students': reverse('student-list', request=request, format=format),
    })