from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.JobPostList.as_view()),
    path('company', views.CompanyCreate.as_view()),
    path('jobpost/<int:pk>/', views.JobPostDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)