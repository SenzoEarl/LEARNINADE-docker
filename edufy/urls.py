from django.urls import path, include

from edufy.views import *

app_name = 'edufy'
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('manage/course', ManageCourseListView.as_view(), name='manage_course_list'),

    path('course/create/', CourseCreateView.as_view(), name='course_create'),
    path('course/<pk>/edit/', CourseUpdateView.as_view(), name='course_edit'),
    path('course/<pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),

    path('course/module/<pk>/', CourseModuleUpdateView.as_view(), name='course_module_update'),

    path('module/<int:module_id>/content/<model_name>/create/', ContentCreateUpdateView.as_view(),
         name='module_content_create'),
    path('module/<int:module_id>/content/<model_name>/<id>/', ContentCreateUpdateView.as_view(),
         name='module_content_update'),
    path('content/<int:id>/delete/', ContentDeleteView.as_view(), name='module_content_delete'),
    path('module/<int:module_id>/', ModuleContentListView.as_view(), name='module_content_list'),

    path('module/order/', ModuleOrderView.as_view(), name='module_order'),
    path('content/order/', ContentOrderView.as_view(), name='content_order'),


    path('subject/list/', SubjectList.as_view(), name='all-subject-list'),
    path('subject/<slug:subject>/', CourseListView.as_view(), name='course_list_subject'),
    path('overview/<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),
]
