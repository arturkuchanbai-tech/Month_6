from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer
from .models import ConfirmationCode


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        confirmation, created = ConfirmationCode.objects.get_or_create(user=user)
        confirmation.code = ConfirmationCode.generate_code()
        confirmation.save()

        print(f"Confirmation code for {user.username}: {confirmation.code}")

        return Response(data={'user_id': user.id},status=status.HTTP_201_CREATED)


class ConfirmUserAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        code = request.data.get('code')

        user = User.objects.filter(username=username).first()
        if not user:
            return Response({'error': 'User not found'}, status=404)

        confirmation = ConfirmationCode.objects.filter(user=user).first()
        if not confirmation:
            return Response({'error': 'Code not found'}, status=404)

        if confirmation.is_expired():
            return Response({'error': 'Code expired'}, status=400)

        if confirmation.code != code:
            return Response({'error': 'Invalid code'}, status=400)

        user.is_active = True
        user.save()
        confirmation.delete()

        return Response({'message': 'User confirmed'}, status=200)


class AuthorizationAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        if not user.is_active:
            return Response({'error': 'User is not confirmed'},status=status.HTTP_403_FORBIDDEN)

        token, _= Token.objects.get_or_create(user=user)

        return Response({'key': token.key})
    
