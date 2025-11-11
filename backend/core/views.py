from rest_framework import viewsets, permissions
from .models import Patient, MedicalRecord, CaseStudy, Assessment
from .serializers import PatientSerializer, MedicalRecordSerializer, CaseStudySerializer, AssessmentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class IsPractitioner(permissions.BasePermission):
    def has_permission(self, request, view):
        return getattr(request.user, "role", None) == "practitioner" or request.user.is_superuser

class IsLecturer(permissions.BasePermission):
    def has_permission(self, request, view):
        return getattr(request.user, "role", None) == "lecturer" or request.user.is_superuser
    
class IsLecturerOrPractitioner(permissions.BasePermission):
    def has_permission(self, request, view):
        return getattr(request.user, "role", None) in ("lecturer", "practitioner") or request.user.is_superuser

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by("-created_at")
    serializer_class = PatientSerializer

    def get_permissions(self):
        if self.action in ["create","update","partial_update","destroy"]:
            return [IsPractitioner()]
        return [permissions.IsAuthenticated()]

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all().order_by("-created_at")
    serializer_class = MedicalRecordSerializer

    def get_permissions(self):
        if self.action in ["create"]:
            return [IsPractitioner()]
        return [permissions.IsAuthenticated()]

class CaseStudyViewSet(viewsets.ModelViewSet):
    queryset = CaseStudy.objects.all().order_by("-created_at")
    serializer_class = CaseStudySerializer

    def get_permissions(self):
        if self.action in ["create"]:
            # return [permissions.IsLecturer() | IsPractitioner()] 
            return [IsLecturerOrPractitioner()]
        return [permissions.IsAuthenticated()]

class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all().order_by("-submitted_at")
    serializer_class = AssessmentSerializer

    def get_permissions(self):
        if self.action in ["create"]:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticated()]
