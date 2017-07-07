# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

STANDARD_CHOICES = (
    (1, 'I'),
    (2, 'II'),
    (3, 'III'),
    (4, 'IV'),
    (5, 'V'),
    (6, 'VI'),
    (7, 'VII'),
    (8, 'VIII'),
    (9, 'IX'),
    (10, 'X')
)


class CommonInfo(models.Model):
	"""
	Common Informations for Student, School model
	"""
	name = models.CharField(max_length=32)
	image = models.ImageField(upload_to='image/%Y/%m', null=True, blank=True)

	class Meta:
		abstract = True
		

class Student(CommonInfo):
	"""
	Student Informations model
	"""
	standard = models.IntegerField(choices=STANDARD_CHOICES, default=1)

	def __str__(self):
		return self.name


class School(CommonInfo):
	"""
	School Informations model
	"""
	address = models.TextField()
	students = models.ManyToManyField(Student, blank=True, db_index=True, related_name='school')

	def __str__(self):
		return self.name