from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TeacherViewSet, ClassPackViewSet, InstrumentViewSet, PriceViewSet,
    ClassViewSet, LevelViewSet, TeacherClassViewSet, StudentViewSet,
    EnrollmentViewSet, ClassPackDiscountRuleViewSet, ClassPackClassViewSet,
    home, create_enrollment, create_student, create_instrument, create_teacher,
    delete_teacher, edit_teacher, create_class_pack, edit_class_pack, delete_class_pack,
    execute_query_month, execute_query_total_due
)

router = DefaultRouter()
router.register(r'teacher', TeacherViewSet)
router.register(r'class_pack', ClassPackViewSet)
router.register(r'instrument', InstrumentViewSet)
router.register(r'price', PriceViewSet)
router.register(r'class', ClassViewSet)
router.register(r'level', LevelViewSet)
router.register(r'teacher_class', TeacherClassViewSet)
router.register(r'student', StudentViewSet)
router.register(r'enrollment', EnrollmentViewSet)
router.register(r'class_pack_discount_rule', ClassPackDiscountRuleViewSet)
router.register(r'class_pack_class', ClassPackClassViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('create-enrollment/', create_enrollment, name='create_enrollment'),
    path('create-student/', create_student, name='create_student'),
    path('create-teacher/', create_teacher, name='create_teacher'),
    path('create-instrument/', create_instrument, name='create_instrument'),
    path('delete-teacher/<int:teacher_id>/', delete_teacher, name='confirm_delete_teacher'),
    path('edit-teacher/<int:teacher_id>/', edit_teacher, name='edit_teacher'),
    path('create-class-pack/', create_class_pack, name='create_class_pack'),
    path('edit-class-pack/<int:pk>/', edit_class_pack, name='edit_class_pack'),
    path('delete-class-pack/<int:pk>/', delete_class_pack, name='confirm_delete_class_pack'),
    path('execute-query-month/', execute_query_month, name='query_results_month'),
    path('execute-query-total-due/', execute_query_total_due, name='query_results_total_due'),
    path('', include(router.urls)),
]
