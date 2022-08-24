from .models import Company
from .models import JobPost
from .models import User
from .models import Resume
from rest_framework import serializers

# 회사 등록
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

# 채용공고 등록
class JobpostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'

# 채용공고 상세 조회
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

# 사용자 등록, 삭제
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# 이력서 등록, 조회, 삭제
class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'