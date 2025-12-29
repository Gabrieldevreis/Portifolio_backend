from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProjectView

router= DefaultRouter()
router.register('projects',ProjectView)

urlpatterns = router.urls
