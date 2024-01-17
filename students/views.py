from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
# Create your views here:


@api_view(['GET'])
def students_list_view(request):
    students = Student.objects.all()
    students_serializer = StudentSerializer(students, many=True)
    return Response(students_serializer.data)


@api_view(['GET'])
def student_detail_view(request, pk):
    student = Student.objects.get(id=pk)
    student_serializer = StudentSerializer(student, many=False)
    return Response(student_serializer.data)


@api_view(['POST'])
def student_save_view(request):  # def save is create
    student = StudentSerializer(data=request.data)
    if student.is_valid():
        student.save()
    return Response(student.data)


@api_view(['POST'])
def student_update_view(request, pk):
    instance = Student.objects.get(id=pk)
    student = StudentSerializer.objects.get(instance=instance, data=request.data)

    if student.is_valid():
        student.save()
    return Response(student.data)


@api_view(['DELETE'])
def student_delete_view(request, pk):
    instance = Student.objects.get(id=pk)
    instance.delete()
    return Response(f"Student Number {pk} Deleted!")
