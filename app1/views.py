from django.shortcuts import render,redirect
from app1.models import principles,HOD,profissors,students
from app1.form import principle_form,hod_form,profissor_form,students_form
from app1.form1 import principle_update_form,profissor_update_form,hod_update_form,students_update_form
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def registration_form(request):
    message=''
    if request.method=='POST':
        username=request.POST.get('username')
        user_email=request.POST.get('useremail')
        p1=request.POST.get('user_password')
        p2=request.POST.get('user_con_password')

        if p1!=p2:
            message='enter correct password'

        elif User.objects.filter(email=user_email).exists():
            message='user Exit'

        else:
            user=User.objects.create_user(username=username,email=user_email,password=p1)
            user.save()
            message='user created'
            return redirect('login101')

    return render(request,'regi/register.html',{'message':message})

def login_form(request):
    message=''

    if request.method=='POST':

        username=request.POST.get('user_log_name')
        password=request.POST.get('user_log_password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            message='login sucessfully'
            return redirect('home')

        else:
            message='invalid detaills'

    return  render(request,'regi/rampo.html',{'message':message})

def home(request):
    return render(request,'front/home.html')

def principle_details(request):
    data=principles.objects.all()
    context={
        'data':data
    }
    return render(request,'front_prince/prince.html',context)
def prince_form(request):
    if request.method=='POST':
        form=principle_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prince')
    else:
        form=principle_form()
    context={
        'form':form
    }
    return render(request,'front_prince/price_form.html',context)
def prince_update(request,id):
    data=principles.objects.get(id=id)
    if request.method=='POST':
        form=principle_update_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('prince')
    else:
        form=principle_update_form(instance=data)
    context={
        'form':form
    }
    return render(request,'front_prince/prince_update.html',context)
def prince_delete(request,id):
    data=principles.objects.get(id=id)
    data.delete()
    return redirect('prince')



def hod_details(request):
    data=HOD.objects.all()
    context={
        'data':data
    }
    return render(request,'front_hod/hod.html',context)
def hods_form(request):
    if request.method=='POST':
        form=hod_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hod')
    else:
        form=hod_form()
    context={
        'form':form
    }
    return render(request,'front_hod/hod_form.html',context)
def hod_update(request,id):
    data=HOD.objects.get(id=id)
    if request.method=='POST':
        form=hod_update_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('hod')
    else:
        form=hod_update_form(instance=data)
    context={
        'form':form
    }
    return render(request,'front_hod/hod_update.html',context)
def hod_delete(request,id):
    data=HOD.objects.get(id=id)
    data.delete()
    return redirect('hod')

def profissor_details(request):
    data=profissors.objects.all()
    context={
        'data':data
    }
    return render(request,'front_profe/profe.html',context)
def profi_form(request):
    if request.method=='POST':
        form=profissor_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profe')
    else:
        form=profissor_form()
    context={
        'form':form
    }
    return render(request,'front_profe/profe_form.html',context)
def profi_update(request,id):
    data=profissors.objects.get(id=id)
    if request.method=='POST':
        form=profissor_update_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('profe')
    else:
        form=profissor_update_form(instance=data)
    context={
        'form':form
    }
    return render(request,'front_profe/profe_update.html',context)
def profi_delete(request,id):
    data=profissors.objects.get(id=id)
    data.delete()
    return redirect('profe')


def student_details(request):
    data=students.objects.all()
    context={
        'data':data
    }
    return render(request,'front_student/student.html',context)
def stu_form(request):
    if request.method=='POST':
        form=students_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stu')
    else:
        form=students_form()
    context={
        'form':form
    }
    return render(request,'front_student/student_form.html',context)
def stu_update(request,id):
    data=students.objects.get(id=id)
    if request.method=='POST':
        form=students_update_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('stu')
    else:
        form=students_update_form(instance=data)
    context={
        'form':form
    }
    return render(request,'front_student/student_update.html',context)
def stu_delete(request,id):
    data=students.objects.get(id=id)
    data.delete()
    return redirect('stu')