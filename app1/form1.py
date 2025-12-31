from django import forms

from app1.models import principles,HOD,profissors,students

class principle_update_form(forms.ModelForm):
    class Meta:
        model=principles
        fields='__all__'

class hod_update_form(forms.ModelForm):
    class Meta:
        model=HOD
        fields='__all__'

class profissor_update_form(forms.ModelForm):
    class Meta:
        model=profissors
        fields='__all__'

class students_update_form(forms.ModelForm):
    class Meta:
        model=students
        fields='__all__'  
        