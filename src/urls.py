from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
   # path('donationfund/', views.ListDonationFund.as_view()),
]
router = DefaultRouter()
router.register(r'donationfund', views.DonationFundViewSet, basename='DonationFund')
urlpatterns += router.urls