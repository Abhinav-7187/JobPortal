from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import JobPost
from .forms import JobPostForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import UserRegistrationForm, EmployerProfileForm, EmployeeProfileForm

def home(request):
    return render(request, 'jobs/home.html')


def employer_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = EmployerProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to the employer dashboard
    else:
        user_form = UserRegistrationForm()
        profile_form = EmployerProfileForm()

    return render(request, 'jobs/employer_register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def employee_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = EmployeeProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to the employee dashboard
    else:
        user_form = UserRegistrationForm()
        profile_form = EmployeeProfileForm()

    return render(request, 'jobs/employee_register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def add_job_post(request):
    if not hasattr(request.user, 'employerprofile'):
        return HttpResponseForbidden("Only employers can add job posts.")
    
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            job_post = form.save(commit=False)
            job_post.employer = request.user.employerprofile  # Associate the job post with the logged-in employer
            job_post.save()
            return redirect('employer_dashboard')  # Redirect to the employer's dashboard
    else:
        form = JobPostForm()
    return render(request, 'jobs/add_job_post.html', {'form': form})
