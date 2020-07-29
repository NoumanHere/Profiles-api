from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    """Test API View"""
    
    def get(self,request,format = None):
        """Returns a list of API View features"""
        an_apiview = [
            'Uses HTTP methods as funtions(get,post,patch,put,delete)',
            'Is similar to a typhical django view',
            'Gives you the most control over the application logic',
            'Is mapped mannually to the URLs'
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})