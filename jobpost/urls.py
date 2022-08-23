from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.JobPostList.as_view()), # 공고 목록 조회
    path('company/', views.CompanyCreate.as_view()), # 회사 등록
    path('jobpost/', views.JobPostCreate.as_view()), # 공고 등록
    path('jobpost/<int:pk>/', views.JobPostDetail.as_view()) # 공고 상세 조회, 수정, 삭제
]

urlpatterns = format_suffix_patterns(urlpatterns)