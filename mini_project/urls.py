"""
URL configuration for mini_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import principle_details,hod_details,profissor_details,student_details
from app1.views import prince_form,hods_form,profi_form,stu_form
from app1.views import prince_update,hod_update,profi_update,stu_update
from app1.views import prince_delete,hod_delete,profi_delete,stu_delete
from app1.views import home
from app1.views import login_form,registration_form


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',login_form,name='login101'),
    path('regist/',registration_form,name='registration101'),

    path('home/',home,name='home'),
    
    path('prince_detail/',principle_details,name='prince'),
    path('prince_form/',prince_form,name='prince_form'),
    path('update/<int:id>',prince_update,name='prince_update'),
    path('del/<int:id>',prince_delete,name='prince_del'),


    path('hod_detail/',hod_details,name='hod'),
    path('hod_form/',hods_form,name='hod_form'),
    path('hod_update/<int:id>',hod_update,name='hod_update'),
    path('hod_del/<int:id>',hod_delete,name='hod_del'),

    path('profe_detail/',profissor_details,name='profe'),
    path('profe_form/',profi_form,name='profe_form'),
    path('profe_update/<int:id>',profi_update,name='profe_update'),
    path('profe_del/<int:id>',profi_delete,name='profe_del'),

    path('student_detail/',student_details,name='stu'),
    path('stu_form/',stu_form,name='stu_form'),
    path('stu_update/<int:id>',stu_update,name='stu_update'),
    path('stu_del/<int:id>',stu_delete,name='stu_del'),
]
