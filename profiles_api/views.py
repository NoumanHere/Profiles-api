from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from . import serializers


class HelloAPIView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerialize
    
    def get(self,request,format = None):
        """Returns a list of API View features"""

        an_apiview = [
            'Uses HTTP methods as funtions(get,post,patch,put,delete)',
            'Is similar to a typhical django view',
            'Gives you the most control over the application logic',
            'Is mapped mannually to the URLs'
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})
    
    def post(self,request):
        """Hello message with our name"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(serializer.errors,
            status = status.HTTP_400_BAD_REQUEST)

    def put(self,request, pk = None):
        """Handle updating an object"""

        return Response({"method":'PUT'})

    def patch(self,request, pk = None):
        """Handle a partial update of an object"""

        return Response({"method":'PATCH'})

    def delete(self,request, pk = None):
        """Delete an object"""

        return Response({"method":'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerialize

    def list(self,request):
        """Returns a hello message"""

        a_viewset = [
            'Uses actions(list,create,retrieve,update,partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more funtionality with the less code',            
        ]

        return Response({'message':'Hello there','a_viewset':a_viewset})

    def create(self,requset):
        """Creates a new hello message"""
        serializer = self.serializer_class(data = requset.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message =  f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
            status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request, pk = None):
        """Handles getting an object by its ID"""
        return Response({'http_method':'GET'})

    def update(self,request, pk = None):
        """Handles updating an object by its ID"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request, pk = None):
        """Handles updaing part of an object by its ID"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request, pk = None):
        """Handles deleting an object by its ID"""
        return Response({'http_method':'DELETE'})