# from rest_framework.views import APIView
# from django.contrib.auth.models import User
# from rest_framework import status
# from rest_framework.response import Response
# from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token
# from .serializers import RegisterSerializer
# from .models import ConfirmationCode

                                                                                                                                                                                                                                                                                                                                                                                                                                
# class ConfirmUserAPIView(APIView):
#     def post(self,request):
#         username = request.data.get('username')
#         code = request.data.get('code')

#         user = User.objects.filter(username=username).first()
#         if not user:
#             return Response({'error':'User not fount'},status=status.HTTP_404_NOT_FOUND)
#         confirmation = ConfirmationCode.objects.filter(user=user).first()
#         if not confirmation:                                                                                                          
#             return Response({'error':'Code not fount'},status=status.HTTP_404_NOT_FOUND)
#         if confirmation.is_expired():
#             return Response({'error':'Code expired'},status=status.HTTP_400_BAD_REQUEST)
#         if confirmation.code!=code:
#             return Response({'error': 'Invalid code'}, status=status.HTTP_400_BAD_REQUEST)
        
#         user.is_active=True
#         user.save()
#         confirmation.delete()
#         return Response({'massage':'user confirmed'}, status=status.HTTP_200_OK)

# class AuthorizationAPIView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('code')
#         user = authenticate(username=username, password=password)
#         if user is None:
#             return Response(status=status.HTTP_403_FORBIDDEN)
#         if not user.is_active():
#             return Response({'error':'User is not confierment'}, status=status.HTTP_403_FORBIDDEN)
#         token, _ =Token.objects.get_or_create(user=user)
#         return Response({'key':token.key})






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
    





# from rest_framework.views import APIView  # Импортируем базовые компоненты для API View
# from django.contrib.auth.models import User  # Импортируем модель User для работы с пользователями
# from rest_framework import status  # Импортируем статус-коды для ответа
# from rest_framework.response import Response  # Импортируем Response для отправки ответов
# from django.contrib.auth import authenticate  # Импортируем функцию для аутентификации пользователя
# from rest_framework.authtoken.models import Token  # Импортируем модель для работы с токенами

# from .serializers import RegisterSerializer  # Импортируем сериализатор для регистрации
# from .models import ConfirmationCode  # Импортируем модель для кода подтверждения

# class RegistrationAPIView(APIView):
#     """
#     Представление для регистрации нового пользователя. Создаёт пользователя и генерирует код подтверждения.
#     """
#     def post(self, request):
#         # Получаем и валидируем данные из запроса через сериализатор
#         serializer = RegisterSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         # Создаём пользователя, если данные валидны
#         user = serializer.save()

#         # Получаем или создаём объект для кода подтверждения для пользователя
#         confirmation, created = ConfirmationCode.objects.get_or_create(user=user)
#         confirmation.code = ConfirmationCode.generate_code()  # Генерируем уникальный код
#         confirmation.save()  # Сохраняем код подтверждения в базе данных

#         print(f"Confirmation code for {user.username}: {confirmation.code}")  # Выводим код в консоль (например, для отправки на email)

#         # Возвращаем ID пользователя в ответе
#         return Response(data={'user_id': user.id}, status=status.HTTP_201_CREATED)

# class ConfirmUserAPIView(APIView):
#     """
#     Представление для подтверждения пользователя по коду. Активирует пользователя, если код правильный.
#     """
#     def post(self, request):
#         username = request.data.get('username')  # Получаем имя пользователя из запроса
#         code = request.data.get('code')  # Получаем код подтверждения из запроса

#         # Ищем пользователя по имени
#         user = User.objects.filter(username=username).first()
#         if not user:
#             return Response({'error': 'User not found'}, status=404)  # Ошибка, если пользователь не найден

#         # Ищем код подтверждения для этого пользователя
#         confirmation = ConfirmationCode.objects.filter(user=user).first()
#         if not confirmation:
#             return Response({'error': 'Code not found'}, status=404)  # Ошибка, если код не найден

#         # Проверяем, истёк ли код
#         if confirmation.is_expired():
#             return Response({'error': 'Code expired'}, status=400)

#         # Проверяем, совпадает ли код
#         if confirmation.code != code:
#             return Response({'error': 'Invalid code'}, status=400)

#         # Активируем пользователя, если код правильный и не истёк
#         user.is_active = True
#         user.save()

#         # Удаляем использованный код
#         confirmation.delete()

#         return Response({'message': 'User confirmed'}, status=200)  # Возвращаем успешный ответ

# class AuthorizationAPIView(APIView):
#     """
#     Представление для авторизации пользователя. Проверяет логин и пароль, выдаёт токен.
#     """
#     def post(self, request):
#         username = request.data.get('username')  # Получаем имя пользователя из запроса
#         password = request.data.get('password')  # Получаем пароль из запроса

#         # Проверяем, существует ли пользователь с такими данными
#         user = authenticate(username=username, password=password)
#         if user is None:
#             return Response(status=status.HTTP_401_UNAUTHORIZED)  # Ошибка, если аутентификация не удалась

#         # Проверяем, активирован ли пользователь
#         if not user.is_active:
#             return Response({'error': 'User is not confirmed'}, status=status.HTTP_403_FORBIDDEN)

#         # Получаем или создаём токен для пользователя
#         token, _ = Token.objects.get_or_create(user=user)

#         # Возвращаем токен в ответе
#         return Response({'key': token.key})  # Токен аутентификации для пользователя