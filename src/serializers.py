from rest_framework import serializer

from src.models import DonationFund


class DonationFundSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField(method_name='get_members')

    class Meta:
        model = DonationFund
        fields = ['name', 'desc', 'members']

    def get_members(self, members):
        pass