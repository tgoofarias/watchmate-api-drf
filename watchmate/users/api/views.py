from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from users.api.serializers import UserSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def account_view(request):
    if request.method == 'GET':
        serializer = UserSerializer(instance=request.user)
        return Response(data=serializer.data)


@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data = dict()
        if serializer.is_valid():
            account = serializer.save()
            token = Token.objects.get(user=account).key
            data['username'] = account.username
            data['email'] = account.email
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data=data)