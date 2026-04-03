from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import ConfirmationCode
from django.contrib.auth import get_user_model


CustomUser = get_user_model()

class UserBaseSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=150)
    password = serializers.CharField()


class AuthValidateSerializer(UserBaseSerializer):
    pass


class RegisterValidateSerializer(UserBaseSerializer):
    def validate_username(self, email):
        try:
            CustomUser.objects.get(email=email)
        except:
            return email
        raise ValidationError('CustomUser уже существует!')


class ConfirmationSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    code = serializers.CharField(max_length=6)

    def validate(self, attrs):
        user_id = attrs.get('user_id')
        code = attrs.get('code')

        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            raise ValidationError('CustomUser не существует!')

        try:
            confirmation_code = ConfirmationCode.objects.get(user=user)
        except ConfirmationCode.DoesNotExist:
            raise ValidationError('Код подтверждения не найден!')

        if confirmation_code.code != code:
            raise ValidationError('Неверный код подтверждения!')

        return attrs

# from rest_framework import serializers
# from django.contrib.auth.models import User
# from django.contrib.auth.password_validation import validate_password
# class RegisterSerializer(serializers.Serializer):
#     username = serializers.CharField(max_langth=150)
#     password = serializers.CharField(write_only =True, min_langth=6)

#     def validate_username(self, username):
#         if User.objects.filter(username=username).exists():
#             raise serializers.ValidationError('User already exists')
#         return username
#     def validate_password(self, password):
#         validate_password(password)
#         return password
#     def create(self,validated_data):
#         user = User.objects.create(username=validated_data['username'], password=validated_data['password'],is_active=False)
#         return user



# from rest_framework import serializers
# from django.contrib.auth.models import User
# from django.contrib.auth.password_validation import validate_password

# class RegisterSerilaizer(serializers.Serializer):
#     username = serializers.CharField(max_langth=150)
#     password = serializers.CharField(write_onlu=True, min_length=6)

#     def validate_username(self, username):
#         if User.objects.filter(username=username).exists():
#             raise serializers.ValidationError('User already exista')
#         return username
    
#     def validate_password(self, password):
#         validate_password(password)
#         return password
    
#     def create(self,validated_data):
#         user = User.objects.create(username=validated_data['username'],password=validated_data['password'], is_active=False)
#         return user



# from rest_framework import serializers  # Импортируем базовые компоненты для сериализатора
# from django.contrib.auth.models import User  # Импортируем модель User для работы с пользователями
# from django.contrib.auth.password_validation import validate_password  # Импортируем встроенную функцию для валидации пароля


# class RegisterSerializer(serializers.Serializer):
#     """
#     Сериализатор для регистрации нового пользователя. Включает проверку уникальности имени пользователя
#     и валидацию пароля.
#     """
#     username = serializers.CharField(max_length=150)  # Поле для имени пользователя с максимальной длиной 150 символов
#     password = serializers.CharField(write_only=True, min_length=6)  # Поле для пароля с минимальной длиной 6 символов

#     def validate_username(self, username):
#         """
#         Проверяет, существует ли уже пользователь с данным именем.
#         Если такой пользователь уже есть, будет вызвана ошибка.
#         """
#         if User.objects.filter(username=username).exists():  # Проверка на наличие пользователя с таким же именем
#             raise serializers.ValidationError('User already exists')  # Ошибка, если имя пользователя уже существует
#         return username

#     def validate_password(self, password):
#         """
#         Валидирует пароль с помощью встроенной проверки Django. Проверяет, соответствует ли пароль 
#         стандартам безопасности, заданным в settings.py.
#         """
#         validate_password(password)  # Проверка пароля по стандартам безопасности (например, длина, сложность и т.д.)
#         return password

#     def create(self, validated_data):
#         """
#         Создаёт нового пользователя с данным именем и паролем. Устанавливает is_active=False, 
#         чтобы пользователь был неактивен до подтверждения по email или через код.
#         """
#         user = User.objects.create_user(
#             username=validated_data['username'],  # Используем переданное имя пользователя
#             password=validated_data['password'],  # Используем переданный пароль
#             is_active=False  # Устанавливаем статус неактивного пользователя до подтверждения
#         )
#         return user