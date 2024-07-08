from rest_framework import serializers
from .models import Teachers, Class_Packs, Instruments, Prices, Classes, Levels, Teacher_Classes, Students, Enrollments, Class_Pack_Discount_Rules, Class_Pack_Classes

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = '__all__'

class ClassPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_Packs
        fields = '__all__'

class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruments
        fields = '__all__'

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prices
        fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Levels
        fields = '__all__'

class TeacherClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher_Classes
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollments
        fields = '__all__'

class ClassPackDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_Pack_Discount_Rules
        fields = '__all__'

class ClassPackClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_Pack_Classes
        fields = '__all__'
