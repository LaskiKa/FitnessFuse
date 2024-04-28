from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from FitnesFuseApp.serializers import (WeightSerializer, StepsSerializer,
                                       ClaoriseBurnedSerializer, TrainingSerializer,
                                       CreateUserSerializer,
                                       LoginUserSerializer, )
from FitnesFuseApp.models import Weight, Steps, ClaoriseBurned, Training
from rest_framework import viewsets, permissions, generics, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

# Create your views here.

class CreateUser(generics.GenericAPIView):
    """
    Register new user endpoint
    """
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message": "User successfully created"
        })

class LoginUser(APIView):
    serializer_class = LoginUserSerializer

    def post(self, requset):
        username = requset.data.get("username")
        password = requset.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            # Invalidate user tokens
            Token.objects.filter(user=user).delete()

            # Create or update user token
            token, created = Token.objects.get_or_create(user=user)

            # return Response({"token": user.auth_token.key})
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class LogoutUser(APIView):

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    def post(self, request):
        token = request.data.get("token")
        Token.objects.filter(key=token).delete()
        return Response({"message": "You are logged out"}, status=status.HTTP_200_OK)




class WeightViewSet(viewsets.ModelViewSet, CreateModelMixin, UpdateModelMixin):
    """
    API Weight endpoint - viewing and editing
    """
    serializer_class = WeightSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication, SessionAuthentication,)
    def get_queryset(self):
        return Weight.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        token = request.data.get('user')
        request.data['user'] = Token.objects.get(key=token).user.pk
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):\

        token = request.data.get('user')
        request.data['user'] = Token.objects.get(key=token).user.pk

        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class StepsViewSet(viewsets.ModelViewSet):
    """
    API Steps endpoint - viewing and editing
    """
    serializer_class = StepsSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,SessionAuthentication,)


    def get_queryset(self):
        return Steps.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        token = request.data.get('user')
        request.data['user'] = Token.objects.get(key=token).user.pk
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):

        token = request.data.get('user')
        request.data['user'] = Token.objects.get(key=token).user.pk

        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(data=serializer.data, status=status.HTTP_200_OK)



class ClaoriseBurnedViewSet(viewsets.ModelViewSet):
    """
    API Calories endpoint - viewing and editing
    """
    serializer_class = ClaoriseBurnedSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return ClaoriseBurned.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        token = request.data.get('user')
        request.data['user'] = Token.objects.get(key=token).user.pk
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):\

        token = request.data.get('user')
        request.data['user'] = Token.objects.get(key=token).user.pk

        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(data=serializer.data, status=status.HTTP_200_OK)



class TrainingViewSet(viewsets.ModelViewSet):
    """
    API Training endpoint - viewing and editing
    """
    serializer_class = TrainingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Training.objects.filter(user=self.request.user)



