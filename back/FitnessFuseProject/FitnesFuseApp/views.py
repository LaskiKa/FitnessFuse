from django.shortcuts import render
from FitnesFuseApp.serializers import (WeightSerializer, StepsSerializer,
                                       ClaoriseBurnedSerializer, TrainingSerializer)
from FitnesFuseApp.models import Weight, Steps, ClaoriseBurned, Training
from rest_framework import viewsets, permissions


# Create your views here.

class WeightViewSet(viewsets.ModelViewSet):
    """
    API Weight endpoint - viewing and editing
    """
    serializer_class = WeightSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Weight.objects.filter(user=self.request.user)

class StepsViewSet(viewsets.ModelViewSet):
    """
    API Weight endpoint - viewing and editing
    """
    serializer_class = StepsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Steps.objects.filter(user=self.request.user)

class ClaoriseBurnedViewSet(viewsets.ModelViewSet):
    """
    API Weight endpoint - viewing and editing
    """
    serializer_class = ClaoriseBurnedSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ClaoriseBurned.objects.filter(user=self.request.user)

class TrainingViewSet(viewsets.ModelViewSet):
    """
    API Weight endpoint - viewing and editing
    """
    serializer_class = TrainingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Training.objects.filter(user=self.request.user)

