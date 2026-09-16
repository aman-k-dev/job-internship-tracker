from django.shortcuts import render, redirect, get_object_or_404
from .models import Company, Job, Application
from .forms import CompanyForm, JobForm, ApplicationForm
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
def company_list(request):
    companies = Company.objects.filter(is_active=True)
    return render(
        request,
        "tracker/companies.html",
        {"companies": companies}
    )
@login_required
def company_create(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("company_list")
            
    else:
        form = CompanyForm()
        
    return render (request, "tracker/company_form.html", {"form": form})
@login_required
def company_update(request, id):
    company = Company.objects.get(id=id)
    
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company)
        
        if form.is_valid():
            form.save()
            return redirect("company_list")
        
    else:
        form = CompanyForm(instance=company)
        
    return render(request, "tracker/company_form.html", {"form":form})
@login_required
def company_delete(request, id):
    company = Company.objects.get(id=id)
    if request.method == "POST":
        company.delete()
        return redirect("company_list")
    
    return render(
        request,
        "tracker/company_confirm_delete.html",
        {"company": company}
    )
@login_required
def job_list(request):
    status = request.GET.get("status")
    location = request.GET.get("location")
    search = request.GET.get("search")
    jobs = Job.objects.all()
    if status:
        jobs = jobs.filter(status=status)
    if location:
        jobs = jobs.filter(location=location)
    if search:
        jobs = jobs.filter(title__icontains=search)
        
    return render(
        request,
        "tracker/jobs.html",
        {
            "jobs": jobs,
            "status": status,
            "location": location,
            "search": search,
        }
    )
@login_required
def job_create(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("job_list")
        
    else:
        form = JobForm()
        
    return render(request,"tracker/job_form.html", {"form": form})
@login_required
def job_update(request, id):
    job = Job.objects.get(id=id)
    
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        
        if form.is_valid():
            form.save()
            return redirect("job_list")
    
    else:
        form = JobForm(instance=job)
        
    return render(request, "tracker/job_form.html", {"form":form})
@login_required
def job_delete(request, id):
    job = Job.objects.get(id=id)
    if request.method == "POST":
        job.delete()
        return redirect("job_list")
    
    return render(
        request,
        "tracker/job_confirm_delete.html",
        {"job": job}
    )
@login_required
def application_list(request):
    applications = Application.objects.filter(user=request.user)
    return render(
        request,
        "tracker/applications.html",
        {"applications":applications}
    )
@login_required
def application_create(request):

    if request.method == "POST":

        form = ApplicationForm(request.POST)

        if form.is_valid():

            application = form.save(commit=False)
            application.user = request.user
            application.save()

            return redirect("application_list")

    else:
        form = ApplicationForm()

    return render(
        request,
        "tracker/application_form.html",
        {"form": form}
    )
@login_required
def application_update(request, id):
    application = get_object_or_404(
    Application,
    id=id,
    user=request.user
    )
    if request.method == "POST":
        form = ApplicationForm(request.POST, instance=application)
        
        if form.is_valid():
            form.save()
            return redirect("application_list")
        
    else:
        form = ApplicationForm(instance=application)
    return render(
        request,
        "tracker/application_form.html",
        {"form": form}
    )
@login_required
def application_delete(request, id):
    application = get_object_or_404(
    Application,
    id=id,
    user=request.user
    )
    if request.method == "POST":
        application.delete()
        return redirect("application_list")
    
    return render(
        request,
        "tracker/application_confirm_form.html",
        {"application": application}
    )
@login_required
def dashboard(request):
    companies = Company.objects.count()
    jobs = Job.objects.count()

    user_applications = Application.objects.filter(user=request.user)

    applications = user_applications.count()
    applied = user_applications.filter(status="APPLIED").count()
    interview = user_applications.filter(status="INTERVIEW").count()
    offers = user_applications.filter(status="OFFER").count()
    recent_applications = user_applications.order_by("-applied_date")[:5]

    return render(
        request,
        "tracker/dashboard.html",
        {
            "companies": companies,
            "jobs": jobs,
            "applications": applications,
            "applied": applied,
            "interview": interview,
            "offers": offers,
            "recent_applications": recent_applications,
        }
    )
@login_required
def register_view(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login_page")

    return render(request, "tracker/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")

    return render(request, "tracker/login.html")