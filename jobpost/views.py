from django.shortcuts import render
from .models import Company
from .models import JobPost
from .serializer import CompanySerializer
from .serializer import JobpostSerializer
from .serializer import JobpostCreateSerializer
from .serializer import JobpostListSerializer
from rest_framework import generics
from rest_framework.filters import SearchFilter

# 회사 등록
class CompanyCreate(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

# 공고 목록 조회
class JobPostList(generics.ListAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobpostListSerializer

# 공고 등록
class JobPostCreate(generics.CreateAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobpostCreateSerializer

# 공고 상세 조회, 수정, 삭제
class JobPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobpostSerializer

