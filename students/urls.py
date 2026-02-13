from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.studentlist, name='student_list'),
    path('<int:id>/',views.student_detail,name='student_detail'),
    path('<int:id>/edit/', views.student_update, name='student_update'),
    path('add/',views.student_add,name="student_add"),
]