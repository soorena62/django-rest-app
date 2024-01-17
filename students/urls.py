from django.urls import path
from .views import StudentSerializer, students_list_view, student_detail_view, student_save_view, student_update_view, \
    student_delete_view

urlpatterns = [
    path('student_list', students_list_view),
    path('student_detail/<pk>', student_detail_view),
    path('student_save', student_save_view),
    path('student_update/<pk>', student_update_view),
    path('student_delete/<pk>', student_delete_view),

]
