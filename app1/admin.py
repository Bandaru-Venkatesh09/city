from django.contrib import admin

from app1.models import principles,HOD,profissors,students

class principle_admin(admin.ModelAdmin):
    list_display=['Name','Emp_Id','Phone_No','Email','Join_Date','End_Date']
admin.site.register(principles,principle_admin)

class hod_admin(admin.ModelAdmin):
    list_display=['Name','Emp_Id','Dept','Phone_No','Email']
admin.site.register(HOD,hod_admin)

class professor_admin(admin.ModelAdmin):
    list_display=['Name','Emp_Id','Subj','Phone_No','Email']
admin.site.register(profissors,professor_admin)

class studentd_admin(admin.ModelAdmin):
    list_display=['select','Name','Roll_No','year','Phone_No']
admin.site.register(students,studentd_admin)

