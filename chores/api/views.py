from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from chores.models import Users
from rest_framework import viewsets
from rest_framework.views import APIView
from chores.api.serializers import UsersSerializer


class UsersViewSet(APIView):

    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def get_all(self, request, format=None):
        serializer = UsersSerializer(self.queryset, many=True)
        return Response(serializer.data)


    def get(self, request, format=None):
        username = request.query_params['username']
        queryset = self.queryset.get(username = username)
        serializer = UsersSerializer(queryset)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UsersSerializer(data=request.data)
        username = request.data['username']
        if serializer.is_valid():
            try:
                user = self.queryset.get(username=username) #check if the user already exists
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Users.DoesNotExist:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
