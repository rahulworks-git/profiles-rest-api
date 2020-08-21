from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):

        an_apiview=[
        'Uses HTTP methods as function(get,put,post delete)',
        'is similar to a traditional django view'
        ]
        return Response({'message':'Hello world','an_apiview':an_apiview})

    def post(self, request):
        """create a hello message with our name"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message=f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""

    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return a hello message"""

        a_viewset=[
        'user actions(list,create,retrieve,update,partial update,destroy)',
        'automatically maps to URL using routers',
        'Provides more functionality with lesser code',
        ]
        return Response({'message':'Hello!','a_viewset':a_viewset})
    def create(self,request):
        """create a hello messahe"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})
