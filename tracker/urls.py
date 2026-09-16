from django.urls import path
from . import views

urlpatterns = [
    path("companies/", views.company_list, name = "company_list"),
    path("companies/add/", views.company_create, name="company_create"),
    path("companies/<int:id>/edit/", views.company_update, name="company_update"),
    path("companies/<int:id>/delete/", views.company_delete, name="company_delete"),
    path("jobs/", views.job_list, name = "job_list"),
    path("jobs/add/", views.job_create, name="job_create"),
    path("jobs/<int:id>/edit/", views.job_update, name="job_update"),
    path("jobs/<int:id>/delete/", views.job_delete, name="job_delete"),
    path("applications/", views.application_list, name="application_list"),
    path("applications/add/", views.application_create, name="application_create"),
    path("applications/<int:id>/edit/", views.application_update, name="application_update"),
    path("applications/<int:id>/delete/", views.application_delete, name="application_delete"),
    path("", views.dashboard, name="dashboard"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login_page"),
]