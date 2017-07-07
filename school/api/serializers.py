from rest_framework import serializers
from school.models import Student, School


class StudentSerializer(serializers.HyperlinkedModelSerializer):

    schools = serializers.PrimaryKeyRelatedField(many=True,read_only=False, queryset=School.objects.all(), source='school')
    # schools = serializers.HyperlinkedRelatedField(many=True, view_name='school-detail', read_only=True)

    class Meta:
        model = Student
        fields = ('name', 'image', 'standard', 'url', 'schools')


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    
    students = StudentSerializer(many=True, read_only=True)
    students_ids = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Student.objects.all(), source='students')
    
    #method serializer to sort many to many relation
    # students_listss = serializers.SerializerMethodField('get_students_list')

    # def get_students_list(self, instance):
    #     return Student.objects\
    #         .filter()\
    #         .order_by('name')\
    #         .values_list('name', flat=True)
    
    class Meta:
        model = School
        fields = ('name', 'image', 'address', 'url', 'students', 'students_ids')