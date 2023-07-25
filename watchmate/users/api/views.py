from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.api.serializers import UserSerializer

@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)