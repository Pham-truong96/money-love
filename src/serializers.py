from rest_framework import serializers
from django.contrib.auth.models import User

from src.models import DonationFund


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_superuser']


class DonationFundSerializer(serializers.ModelSerializer):
    members = UserSerializer(read_only=True, many=True)
    class Meta:
        model = DonationFund
        fields = ['id','name', 'desc', 'members']
