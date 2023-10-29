from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import branch1, branch2, branch3, prof

# Create your views here.


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #messages.success(request, "You have been logged in!")
            return redirect('time_table')
        else:
            messages.success(request, "Login unsuccessful...")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def time_table(request):
    username = request.user.username

    if username == 'branch1':
        records = branch1.objects.all()
    elif username == 'branch2':
        records = branch2.objects.all()
    elif username == 'branch3':
        records = branch3.objects.all()
    for record in records:
        record.mon = record.mon.split('_')
        record.mon = record.mon[0] + ' ' + record.mon[1]
        record.tue = record.tue.split('_')
        record.tue = record.tue[0] + ' ' + record.tue[1]
        record.wed = record.wed.split('_')
        record.wed = record.wed[0] + ' ' + record.wed[1]
        record.thu = record.thu.split('_')
        record.thu = record.thu[0] + ' ' + record.thu[1]
        record.fri = record.fri.split('_')
        record.fri = record.fri[0] + ' ' + record.fri[1]

    return render(request, 'time_table.html', {'records': records})

def logout_user(request):
    logout(request)
    return redirect('home')

def update(request):
    if request.method == 'POST':
        return HttpResponse("POST Request Received")
    else:
        result = dict(request.GET)
        # print('Result:',result)
        username = request.user.username
        if username == 'branch2':
            element = int(result['from_sno'][0]) - 1
            x = branch2.objects.all()[element]

            element = int(result['to_sno'][0]) - 1
            y = branch2.objects.all()[element]

            exec(f"x.{result['from_day'][0]}, y.{result['to_day'][0]} = y.{result['to_day'][0]}, x.{result['from_day'][0]}")
            exec(f"print(x.{result['from_day'][0]})")
            exec(f"print(y.{result['to_day'][0]})")
            x.save()
            y.save()
        elif username == 'branch1':
            element = int(result['from_sno'][0]) - 1
            x = branch1.objects.all()[element]

            element = int(result['to_sno'][0]) - 1
            y = branch1.objects.all()[element]

            exec(f"x.{result['from_day'][0]}, y.{result['to_day'][0]} = y.{result['to_day'][0]}, x.{result['from_day'][0]}")
            exec(f"print(x.{result['from_day'][0]})")
            exec(f"print(y.{result['to_day'][0]})")
            x.save()
            y.save()
        elif username == 'branch3':
            element = int(result['from_sno'][0]) - 1
            x = branch3.objects.all()[element]

            element = int(result['to_sno'][0]) - 1
            y = branch3.objects.all()[element]

            exec(f"x.{result['from_day'][0]}, y.{result['to_day'][0]} = y.{result['to_day'][0]}, x.{result['from_day'][0]}")
            exec(f"print(x.{result['from_day'][0]})")
            exec(f"print(y.{result['to_day'][0]})")
            x.save()
            y.save()
        
        return HttpResponse("GET Request Received")
