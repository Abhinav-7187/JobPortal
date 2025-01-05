from django.db import models
from django.contrib.auth.models import User

class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_description = models.TextField()
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.company_name


class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return self.user.username


class JobPost(models.Model):
    title = models.CharField(max_length=255, default="Untitled Job")
    description = models.TextField(default="No description provided.")
    location = models.CharField(max_length=255, default="Default Location")
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE, default=1)
    posted_on = models.DateTimeField(auto_now_add=True)  # No default needed for auto_now_add

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    applied_by = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applied_by.user.username} -> {self.job.title}"



