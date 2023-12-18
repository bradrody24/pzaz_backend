from .models import Book
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def book_list(request):
  if request.method == 'GET':
    user_id = request.user
    books = Book.objects.filter(user=user_id)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
  
  if request.method == 'POST':
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save(user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])    
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def book_detail(request, id):
  try:
    book = Book.objects.get(pk=id)
  except Book.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = BookSerializer(book)
    return Response(serializer.data)
  elif request.method == 'PUT':
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
