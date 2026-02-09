from django.urls import path,include
from . import views

urlpatterns = [
    path('studentlist/', views.studentlist, name='student_list'),
    path('student/<int:id>/',views.student_detail,name='student_detail'),

]