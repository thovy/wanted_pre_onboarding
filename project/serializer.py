from .models import Company
from .models import JobPost
from rest_framework import serializers

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class JobpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'