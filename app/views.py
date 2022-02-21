from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from rest_framework.decorators import api_view
@api_view(['POST'])
def post(request):
    if request.method == 'POST':
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)