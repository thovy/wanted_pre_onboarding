from django.shortcuts import render
from .models import Company
from .models import JobPost
from .models import User
from .models import Resume
from .serializer import CompanySerializer
from .serializer import JobpostSerializer
from .serializer import JobpostCreateSerializer
from .serializer import JobpostListSerializer
from .serializer import UserSerializer
from .serializer import ResumeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

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

# 공고 검색
class JobPostSearch(ModelViewSet):
    gueryset = JobPost.objects.all()
    serializer_class = JobpostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'skill']


# 사용자 등록
class UserCreate(generics.CreateAPIView):
    queryset = User
    serializer_class = UserSerializer

# 사용자 조회, 수정, 삭제
class UserUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User
    serializer_class = UserSerializer

# 이력서 등록
class ResumeCreate(generics.CreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

# 이력서 조회, 삭제
class ResumeDelete(generics.RetrieveDestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

