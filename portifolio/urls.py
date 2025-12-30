from rest_framework.routers import DefaultRouter
from .views import (
    ProjectView,
    ProfileView,
    CertificateView,
    ExperienceView
)

router = DefaultRouter()
router.register('projects', ProjectView)
router.register('profile', ProfileView)
router.register('certificate', CertificateView)
router.register('experience', ExperienceView)

urlpatterns = router.urls
