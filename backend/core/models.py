from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Basic role system; expand later into groups/permissions
    ROLE_CHOICES = (
        ("practitioner","Practitioner"),
        ("student","Student"),
        ("lecturer","Lecturer"),
        ("admin","Admin"),
    )
    role = models.CharField(max_length=32, choices=ROLE_CHOICES, default="student")
    # Add fields like institution, license_number, etc.
    license_number = models.CharField(max_length=128, blank=True, null=True)

    def is_practitioner(self):
        return self.role == "practitioner"

    def is_student(self):
        return self.role == "student"

    def is_lecturer(self):
        return self.role == "lecturer"

class Patient(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    dob = models.DateField(null=True, blank=True)
    medical_record_number = models.CharField(max_length=128, unique=True)
    # minimal PII; store sensitive fields encrypted in prod
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="patients_created")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.medical_record_number})"

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="records")
    note = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # tags, attachments stored elsewhere (S3) with links
    attachments = models.JSONField(default=list, blank=True)

class CaseStudy(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tags = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    media_urls = models.JSONField(default=list, blank=True)  # links to S3, etc.
    is_public = models.BooleanField(default=False)

class Assessment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assessments")
    evaluator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="evaluations")
    case_study = models.ForeignKey(CaseStudy, on_delete=models.SET_NULL, null=True, blank=True)
    score = models.FloatField(null=True, blank=True)
    feedback = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
