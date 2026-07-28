from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

# Public view accessible without authentication
@api_view(['GET'])
@permission_classes([AllowAny])

def public_view(request):
    return Response({"message": 'This is  a public view accessible to everyone'}) 


# Private view accessible only to authenticated users
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def private_view(request):
    return Response({'message':f"Hello,{request.user.username}, This is a private view accessible to authenticated users" }) 
