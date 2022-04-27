from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from django.shortcuts import redirect
from .forms import employeeform
from django.contrib import messages
# Create your views here.

def Home(request):
    e = Employee.objects.all()
    e = e.values()
    ae = Employee.objects.filter(Active= True)
    le = Employee.objects.filter(on_leave=True)
    context = {'e':e ,'ae':ae,'le':le}
    return render(request,'Home.html',context)


def Create(request):
    # e = Employee.objects.create()
    if request.method == 'POST':
        
        emp = Employee.objects.filter(Name=request.POST['Name'])
        if not emp.exists():
            print(request.POST)
            print('Name',request.POST['Name'])
            print('DOB',request.POST['DOB'])
            e = Employee.objects.create(Name=request.POST['Name'],DOB=request.POST['DOB'],Department=request.POST['Department'],
            post=request.POST['post'],Address=request.POST['Address'],
            City=request.POST['City'],Country=request.POST['Country'],
            ZipCode=request.POST['ZipCode'],State=request.POST['State'],
            DOJ=request.POST['DOJ'],)
            
        else:
            return HttpResponse('Employee name already exist')
        return redirect('Employee_List')
    return render(request,'Create.html')

def Edit_Employee(request,myid):
        e = Employee.objects.get(Id = myid)
        form = employeeform(instance=e)
        if request.method == 'POST':
            form = employeeform(request.POST, instance=e)
            if form.is_valid():
                form.save()
                messages.info(request,'Your Details Updated Successfully ')
                return redirect('Employee_List')
        context = {'form':form}
        return render(request, 'Edit_Employee.html',context)
        #

def Employee_List(request):
    emp = Employee.objects.all()
    emp = emp.values()
    # print(emp)
    context = {'emp':emp }

    return render(request, 'Employee_List.html', context)

def delete_view(request,myid):

        e = Employee.objects.get(Id = myid)
        if request.method == 'POST':
            e.delete()
            messages.info(request,'Employee is deleted')
            return redirect('Employee_List')

        context = {'e':e}
        return render(request, 'delete_view.html',context)

def leave(request,id):

        e = Employee.objects.get(Id = id)
        if e.on_leave:
            e.on_leave = False
        else:
            e.on_leave = True
            e.Leave_count += 1
        e.save()
        return redirect('Employee_List')
