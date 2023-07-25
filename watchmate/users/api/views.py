from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from users.api.serializers import UserSerializer


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