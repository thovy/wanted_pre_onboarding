from .models import Company
from .models import JobPost
from rest_framework import serializers

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

# 채용공고 리스트 조회
class JobpostListSerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField(source='company.name')
    company_nation = serializers.ReadOnlyField(source='company.nation')
    company_region = serializers.ReadOnlyField(source='company.region')

    class Meta:
        model = JobPost
        fields = [
            "id",
            "company_name",
            "company_nation",
            "company_region",
            "position",
            "reward",
            "skill",
        ]

class JobpostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'

# 채용공고 전체 조회
class JobpostSerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField(source='company.name')
    company_nation = serializers.ReadOnlyField(source='company.nation')
    company_region = serializers.ReadOnlyField(source='company.region')

    class Meta:
        model = JobPost
        fields = [
            "id",
            "company_name",
            "company_nation",
            "company_region",
            "position",
            "reward",
            "skill",
            "article",
        ]