from django.shortcuts import render, redirect
import requests
import json
# Create your views here:


def students_list_view(request):
    response = requests.get('http://127.0.0.1:8000/students/student_list').json()

    context = {
        "students": response
    }

    return render(request, 'rest_test/student-list.html', context)


def student_save_view(request):
    instance = {"first_name": "Rojina", "last_name": "Negahdari", "id_code": "1395"}
    json_data = json.dumps(instance)
    headers = {'content-type': 'application/json'}
    requests.post('http://127.0.0.1:8000/students/student_save', data=json_data, headers=headers)
    return redirect(students_list_view)
