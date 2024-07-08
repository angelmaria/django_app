# api/forms.py

from django import forms
from .models import Enrollments, Students

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollments
        fields = '__all__'  # Todos los campos del modelo Enrollment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'  # Todos los campos del modelo Student
