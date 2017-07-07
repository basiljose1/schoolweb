# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from school.models import Student, School
from django.contrib.auth.models import User, Group

# Register / Unregister your models here.
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(School)
admin.site.register(Student)

