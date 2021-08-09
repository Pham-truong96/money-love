from django_filters import rest_framework as filters
import django_filters

from src.models import DonationFund


class DonationFundFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="contains")
    desc = filters.CharFilter(field_name="desc", lookup_expr="contains")

    class Meta:
        model = DonationFund
        fields = ['id', 'name', 'desc']
