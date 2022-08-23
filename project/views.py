from django.shortcuts import render
from .models import JobPost
from .serializer import JobpostSerializer
from rest_framework import generics

# 목록 조회, 등록
class JobPostList(generics.ListCreateAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobpostSerializer

# 조회, 수정, 삭제
class JobPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobpostSerializer

