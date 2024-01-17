from django.urls import path

from .views import students_list_view, student_save_view

urlpatterns = [
    path('student_list', students_list_view),
    path('student_save', student_save_view),

]
