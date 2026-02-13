from django.urls import path,include
from . import views

urlpatterns = [
    path('studentlist/', views.studentlist, name='student_list'),
    path('student/<int:id>/',views.student_detail,name='student_detail'),
    path('student/<int:id>/edit', views.student_update, name='student_update'),
]