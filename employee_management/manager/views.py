from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
import json
from .forms import PositionForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def positions(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, post, category FROM public.positions;")
        positions = cursor.fetchall()
    
    data = [{'id': p[0], 'post': p[1], 'category': p[2]} for p in positions]
    return JsonResponse(data, safe=False)

def employee_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, post FROM public.positions;")
        positions = cursor.fetchall()
    data = [{'id': p[0], 'post': p[1]} for p in positions]
    return render(request, 'manager/employee/employee_list.html', {'data': data})

@csrf_exempt
def add_positions(request):
    if request.method == "POST":
        post = request.POST.get('post')
        category = request.POST.get('category')

        if not post or not category:
            return JsonResponse({'status': 'error', 'message': 'Некорректно введены данные'})

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO positions (post, category) VALUES (%s, %s)", (post, category))
            return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})

@csrf_exempt
def delete_positions(request):
    if request.method == "POST":
        pk = request.POST.get('id')
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM positions WHERE id = (%s)", (pk,) )
            return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})

def positions_templates(request):
    return render(request, 'manager/positions/positions.html')     

def position_view(request, pk):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, post, category FROM public.positions WHERE (positions.id = (%s))", (pk,))
        position = cursor.fetchone()
    data = {'id': position[0], 'post': position[1], 'category': position[2]}
    return render(request, 'manager/positions/position.html', {'data': data})

def position_template(request):
    return render(request, 'manager/positions/position.html')

@csrf_exempt
def position_update(request):
    if request.method == "POST":
        post = request.POST.get('post')
        category = request.POST.get('category')
        id = request.POST.get('id')
        if post == '': 
            return JsonResponse({'status': 'error', 'message': 'Некорректно введены данные'})
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE positions 
                           SET post = (%s),
                            category = (%s) 
                           WHERE positions.id=(%s)""", (post, category, id))
            return JsonResponse({'status': 'ok', "message": 'Успешно'})
    return JsonResponse({'status': 'error'})

def employees(request):
    with connection.cursor() as cursor:
        cursor.execute("select * from employees e join positions p on e.position_id = p.id;")
        employees = cursor.fetchall()
    data = [{'id': e[0], 'lastName': e[1], 'firstName': e[2], 'patronymic': e[3], 'sex': e[4], 'age': e[5], 'post': e[8], 'category': e[9]} for e in employees]
    return JsonResponse(data, safe=False)

@csrf_exempt
def add_employee(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        patronymic = request.POST.get('patronymic')
        if firstname == '' or lastname == '' or patronymic == '':
            return JsonResponse({'status':'error', "message": 'Неверно введено ФИО'})
        sex = request.POST.get('sex')
        try:
            age = int(request.POST.get('age'))
            if age <= 17 or age >= 65:
                return JsonResponse({'status':'error', "message": 'Неверно введен возраст'})
        except: 
            return JsonResponse({'status':'error', "message": 'Неверно введен возраст'})
        post = request.POST.get('post')
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO employees (first_name, last_name, patronymic, sex, age, position_id) VALUES (%s, %s, %s, %s,%s, %s)", (firstname, lastname, patronymic, sex, age, post))
            return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})

@csrf_exempt
def delete_employee(request):
    if request.method == "POST":
        pk = request.POST.get('id')
        print(pk)
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM public.employees WHERE id=(%s)", (pk,) )
            return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})

@csrf_exempt
def employee_update(request):
    if request.method == "POST":
        lastname = request.POST.get('lastname')
        firstname = request.POST.get('fifirstnameo')
        patronymic = request.POST.get('patronymic')
        if lastname == '' or firstname == '' or patronymic == '':
            return JsonResponse({'status':'error', "message": 'Неверно введено ФИО'})
        sex = request.POST.get('sex')
        try:
            age = int(request.POST.get('age'))
            if age <= 17 or age >= 65:
                return JsonResponse({'status':'error', "message": 'Неверно введен возраст'})
        except: 
            return JsonResponse({'status':'error', "message": 'Неверно введен возраст'})
        position_id = request.POST.get('post')
        id = request.POST.get('id')
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE employees 
                           SET last_name = (%s),
                           first_name = (%s),
                           patronymic = (%s),
                            sex = (%s) ,
                           age = (%s),
                           position_id = (%s)
                           WHERE employees.id=(%s)""", (lastname, firstname, patronymic, sex, age, position_id, id))
            return JsonResponse({'status':'ok', "message": 'Успешно!'})
    return JsonResponse({'status': 'error'})

def employee_view(request, pk):
    with connection.cursor() as cursor:
        cursor.execute("SELECT employees.id, last_name, first_name, patronymic, sex, age, post FROM public.employees join positions on employees.position_id = positions.id WHERE employees.id = (%s);", (pk,))
        employee = cursor.fetchone()
        cursor.execute("SELECT id, post FROM public.positions")
        post = cursor.fetchall()
    data_post = [{'id': p[0], 'post': p[1]} for p in post]
    data_employee = {'id': employee[0], 'lastname': employee[1], 'firstname': employee[2], 'patronymic': employee[3], 'sex': employee[4], 'age': employee[5], 'post': employee[6]}
    return render(request, 'manager/employee/employee.html', {'data_employee': data_employee,
                                                               'data_post': data_post})