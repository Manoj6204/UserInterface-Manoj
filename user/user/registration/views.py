from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

# GET /user/getAll - Get all users
@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# GET /user/get?rollno=101 - Get a single user by rollno
@api_view(['GET'])
def get_user(request):
    rollno = request.GET.get('rollno')
    if not rollno:
        return Response({'error': 'rollno parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(rollno=rollno)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

# POST /user/create - Create a new user
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# PUT /user/update - Update an existing user by rollno
@api_view(['PUT'])
def update_user(request):
    rollno = request.data.get('rollno')
    if not rollno:
        return Response({'error': 'rollno field is required for update'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(rollno=rollno)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

# DELETE /user/delete?rollno=101 - Delete a user by rollno
@api_view(['DELETE'])
def delete_user(request):
    rollno = request.GET.get('rollno')
    if not rollno:
        return Response({'error': 'rollno parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(rollno=rollno)
        user.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
