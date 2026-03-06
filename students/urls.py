
from django.urls import path
from . import views

urlpatterns = [

path('',views.student_list),

path('add/',views.add_student),

path('delete/<int:id>/',views.delete_student),

]