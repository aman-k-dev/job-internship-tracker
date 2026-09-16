from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    website = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Profile(models.Model):

    ROLE_CHOICES = [
        ("APPLICANT", "Applicant"),
        ("COMPANY_REP", "Company Representative"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="APPLICANT"
    )

class Job(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name="jobs"
    )
    title = models.CharField(max_length=150)
    location = models.CharField(max_length=150, blank=True)
    salary_min = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )
    salary_max = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )
    status = models.CharField(max_length=20, default="OPEN")

    def __str__(self):
        return f"{self.company.name} - {self.title}"

class Application(models.Model):
    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name="applications"
    )
    
    STATUS_CHOICES = [
        ("APPLIED", "Applied"),
        ("OA", "Online Assessment"),
        ("INTERVIEW", "Interview"),
        ("REJECTED", "Rejected"),
        ("OFFER", "Offer"),
        ("WITHDRAWN", "Withdrawn"),
    ]

    job = models.ForeignKey(
        Job,
        on_delete=models.PROTECT,
        related_name="applications"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="APPLIED"
    )
    applied_date = models.DateField()
    notes = models.TextField(blank=True)
    
    
    def __str__(self):
        return f"{self.job.title} - {self.status}"