from .serializers import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def signin(request):
  user = get_object_or_404(User, username=request.data['username'])
  if not user.check_password(request.data['password']):
    return Response({"detail": "Credentials does not match"}, status=status.HTTP_401_UNAUTHORIZED)
  token, created = Token.objects.get_or_create(user=user)
  serializer = UserSerializer(instance=user)
  return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def signup(request):
  serializer = UserSerializer(data=request.data)
  if serializer.is_valid():
      serializer.save()
      user = User.objects.get(username=request.data['username'])
      user.set_password(request.data['password'])
      user.save()
      token = Token.objects.create(user=user)
      return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
