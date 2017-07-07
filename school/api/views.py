from rest_framework import generics
from school.models import Student, School
from school.api.serializers import StudentSerializer, SchoolSerializer


class StudentList(generics.ListCreateAPIView):
    """List all students."""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    """Individual Student Details."""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class SchoolList(generics.ListCreateAPIView):
    """List all scholls."""

    queryset = School.objects.all()
    serializer_class = SchoolSerializer



class SchoolDetail(generics.RetrieveUpdateDestroyAPIView):
    """Individual School Details."""

    queryset = School.objects.all()
    serializer_class = SchoolSerializer


    # def perform_create(self, serializer):
    #     property = serializer.save(owner=self.request.user)
    #     property.user.add(self.request.user)