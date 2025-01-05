## Home Page of JobPortal:




![Screenshot 2025-01-05 231902](https://github.com/user-attachments/assets/226227b1-0946-40a3-8bb4-b4a6587f45e9)





### Project Structure:

1) **Models:**

* EmployerProfile: Extended User model for employers.
* EmployeeProfile: Extended User model for employees.
* JobPost: Title, description, requirements, posted_by (FK to EmployerProfile).
* Application: Job FK, applied_by FK to EmployeeProfile, application_date.

2) **Views:**

* Class-based views (CBVs) for CRUD operations.
* DRF for APIs (e.g., job listing, bookmarking, applying).

3) **Templates:**

* Employer Dashboard: Job listing, application details.
* Employee Dashboard: Bookmarked and applied jobs.
* Home, Login, Registration, and Job Details pages.

4) **URLs:**

* /employer/register/, /employer/dashboard/
* /employee/register/, /employee/dashboard/
* /jobs/, /jobs/<id>/apply/, /jobs/<id>/bookmark/

5) **Authentication:**

* Use Django's built-in authentication with @login_required decorators.
* JWT-based authentication if APIs are built for job searching or mobile integration.
