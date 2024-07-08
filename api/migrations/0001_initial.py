# Generated by Django 5.0.6 on 2024-07-08 09:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='ClassPack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Class_Packs',
            },
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Instruments',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'Prices',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('family_discount', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Students',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Teachers',
            },
        ),
        migrations.CreateModel(
            name='ClassPackClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.classpack')),
                ('class_related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.class')),
            ],
            options={
                'db_table': 'Class_Pack_Classes',
            },
        ),
        migrations.CreateModel(
            name='ClassPackDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('class_pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.classpack')),
                ('class_related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.class')),
            ],
            options={
                'db_table': 'Class_Pack_Discount_Rules',
            },
        ),
        migrations.AddField(
            model_name='class',
            name='instrument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.instrument'),
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('class_related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.class')),
            ],
            options={
                'db_table': 'Levels',
            },
        ),
        migrations.AddField(
            model_name='class',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.price'),
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateField()),
                ('class_number', models.IntegerField(default=1)),
                ('class_related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.class')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.level')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.teacher')),
            ],
            options={
                'db_table': 'Enrollments',
            },
        ),
        migrations.CreateModel(
            name='TeacherClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.class')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.teacher')),
            ],
            options={
                'db_table': 'Teacher_Classes',
            },
        ),
    ]
