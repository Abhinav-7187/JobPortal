from django.contrib import admin
from .models import EmployerProfile, EmployeeProfile, JobPost, Application

admin.site.register(EmployerProfile)
admin.site.register(EmployeeProfile)
admin.site.register(JobPost)
admin.site.register(Application)
