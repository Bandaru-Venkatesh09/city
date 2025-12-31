from django.db import models

class principles(models.Model):
    Name=models.CharField(max_length=50)
    Emp_Id=models.IntegerField()
    Phone_No=models.BigIntegerField()
    Email=models.EmailField()
    Join_Date=models.DateField()
    End_Date=models.DateField()


class HOD(models.Model):
    Name=models.CharField(max_length=50)
    Emp_Id=models.IntegerField()
    Dept=models.CharField(max_length=50)
    Phone_No=models.BigIntegerField()
    Email=models.EmailField()


class profissors(models.Model):
    Name=models.CharField(max_length=50)
    Emp_Id=models.IntegerField()
    Subj=models.CharField(max_length=50)
    Phone_No=models.BigIntegerField()
    Email=models.EmailField()
    def __str__(self):
        return self.Name


class students(models.Model):
    select=models.ForeignKey(profissors,on_delete=models.CASCADE)
    Name=models.CharField(max_length=60)
    Roll_No=models.IntegerField()
    year=models.CharField(max_length=10)
    Phone_No=models.BigIntegerField()


