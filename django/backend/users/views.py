from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from rest_framework import status
from django.contrib.auth.models import User

class SignupView(APIView):
    def post(self, request):
        form = UserCreationForm(request.data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return Response({"message": "User created and logged in"}, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({"message": "Logged in successfully"})
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"})
