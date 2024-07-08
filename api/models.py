from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Teachers'

class ClassPack(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Class_Packs'

class Instrument(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Instruments'

class Price(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.amount}'

    class Meta:
        db_table = 'Prices'

class Class(models.Model):
    name = models.CharField(max_length=100)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Classes'

class Level(models.Model):
    name = models.CharField(max_length=100)
    class_related = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Levels'

class TeacherClass(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    class_related = models.ForeignKey(Class, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Teacher_Classes'

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    family_discount = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'Students'

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_related = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True, blank=True)
    enrollment_date = models.DateField()
    class_number = models.IntegerField(default=1)

    class Meta:
        db_table = 'Enrollments'

class ClassPackDiscount(models.Model):
    class_pack = models.ForeignKey(ClassPack, on_delete=models.CASCADE)
    class_related = models.ForeignKey(Class, on_delete=models.CASCADE)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'Class_Pack_Discount_Rules'

class ClassPackClass(models.Model):
    class_pack = models.ForeignKey(ClassPack, on_delete=models.CASCADE)
    class_related = models.ForeignKey(Class, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Class_Pack_Classes'