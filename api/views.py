from rest_framework import viewsets
from .models import Teacher, ClassPack, Instrument, Price, Classes, Levels, TeacherClasses, Students, Enrollments, ClassPackDiscountRules, ClassPackClasses
from .serializers import TeacherSerializer, ClassPackSerializer, InstrumentSerializer, PriceSerializer, ClassesSerializer, LevelsSerializer, TeacherClassesSerializer, StudentsSerializer, EnrollmentsSerializer, ClassPackDiscountRulesSerializer, ClassPackClassesSerializer
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Enrollments, Students
from .forms import EnrollmentForm, StudentForm
from django import forms  # Importas el módulo forms de Django

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class ClassPackViewSet(viewsets.ModelViewSet):
    queryset = ClassPack.objects.all()
    serializer_class = ClassPackSerializer

class InstrumentViewSet(viewsets.ModelViewSet):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer

class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

class ClassesViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

class LevelsViewSet(viewsets.ModelViewSet):
    queryset = Levels.objects.all()
    serializer_class = LevelsSerializer

class TeacherClassesViewSet(viewsets.ModelViewSet):
    queryset = TeacherClasses.objects.all()
    serializer_class = TeacherClassesSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class EnrollmentsViewSet(viewsets.ModelViewSet):
    queryset = Enrollments.objects.all()
    serializer_class = EnrollmentsSerializer

class ClassPackDiscountRulesViewSet(viewsets.ModelViewSet):
    queryset = ClassPackDiscountRules.objects.all()
    serializer_class = ClassPackDiscountRulesSerializer

class ClassPackClassesViewSet(viewsets.ModelViewSet):
    queryset = ClassPackClasses.objects.all()
    serializer_class = ClassPackClassesSerializer

def home(request):
    context = {
        'teachers': Teacher.objects.all(),
        'class_packs': ClassPack.objects.all(),
        'instruments': Instrument.objects.all(),
        'prices': Price.objects.all(),
        'classes': Classes.objects.all(),
        'levels': Levels.objects.all(),
        'teacher_classes': TeacherClasses.objects.all(),
        'students': Students.objects.all(),
        'enrollments': Enrollments.objects.all(),
        'class_pack_discounts': ClassPackDiscountRules.objects.all(),
        'class_pack_classes': ClassPackClasses.objects.all(),
    }
    return render(request, 'api/home.html', context)

def create_enrollment(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirigir a la página principal u otra página después de guardar
    else:
        form = EnrollmentForm()
    
    context = {
        'form': form,
    }
    return render(request, 'api/create_enrollment.html', {'form': form})

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirigir a la página principal u otra página después de guardar
    else:
        form = StudentForm()
    
    context = {
        'form': form,
    }
    return render(request, 'api/create_student.html', context)

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollments
        fields = '__all__'  # Todos los campos del modelo Enrollment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'  # Todos los campos del modelo Student