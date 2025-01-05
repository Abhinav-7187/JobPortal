from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employer/register/', views.employer_register, name='employer_register'),
    path('employee/register/', views.employee_register, name='employee_register'),
    path('employer/add-job/', views.add_job_post, name='add_job_post'),
]
