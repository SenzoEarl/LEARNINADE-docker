from django.urls import path, include
from rest_framework import routers

from . import views
from .views import SubjectListView, SubjectDetailView, CourseViewSet, CourseEnrollView

app_name = 'courses'

router = routers.DefaultRouter()
router.register('edufy', CourseViewSet)

urlpatterns = [
    path('subjects/', SubjectListView.as_view(), name='subject_list'),
    path('subjects/<pk>/', SubjectDetailView.as_view(), name='subject_detail'),
    path('', include(router.urls)),
    path('courses/<pk>/enroll/', CourseEnrollView.as_view(), name='course_enroll'),
]
