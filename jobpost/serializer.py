from .models import Company
from .models import JobPost
from rest_framework import serializers

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

# 채용공고 리스트 조회
class JobpostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = [
            "company_id",
            "position",
            "reward",
            "article",
            "skill",
        ]

# 채용공고 전체 조회
class JobpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'