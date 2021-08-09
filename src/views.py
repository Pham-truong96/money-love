from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import viewsets

from src.filters import DonationFundFilter
from src.models import DonationFund
from src.serializers import DonationFundSerializer


class DonationFundViewSet(viewsets.ModelViewSet):
    queryset = DonationFund.objects.all()
    serializer_class = DonationFundSerializer
    filterset_class = DonationFundFilter
    ordering_fields = ['id', 'desc']
    ordering = ['-id']

    def perform_create(self, serializer):
        instance = serializer.save()
        usernames = self.request.POST.get("members","").split(",")
        usernames.append(self.request.user.username)
        instance.add_member(*User.objects.filter(username__in=usernames))


class ListDonationMembers(generics.ListCreateAPIView):
    pass