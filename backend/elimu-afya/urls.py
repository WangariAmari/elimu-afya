from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import PatientViewSet, MedicalRecordViewSet, CaseStudyViewSet, AssessmentViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r"patients", PatientViewSet)
router.register(r"records", MedicalRecordViewSet)
router.register(r"casestudies", CaseStudyViewSet)
router.register(r"assessments", AssessmentViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(router.urls)),
]
