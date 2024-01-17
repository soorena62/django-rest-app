from rest_framework import serializers
from .models import Student
# Create Your model here:


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
