from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from users.managers import CustomUserManager
from django.core.exceptions import ValidationError


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def clean(self):
        super().clean()
        if self.is_superuser and not self.phone_number:
            raise ValidationError({'phone_number': 'Superuser need have to phone_number.'})

    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email or ''

class ConfirmationCode(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='confirmation_code')
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Код подтверждения для {self.user.email}"




# import random
# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone


# class ConfirmationCode(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     code = models.CharField(max_length=6)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.code}"

#     @staticmethod
#     def generate_code():
#         while True:
#             code = str(random.randint(100000, 999999))
#             if not ConfirmationCode.objects.filter(code=code).exists():
#                 return code

#     def is_expired(self):
#         return timezone.now() > self.created_at + timezone.timedelta(minutes=10)




# from django.db import models
# from django.contrib.auth.models import User
# import random
# from django.utils import timezone

# class ConfirmationCode(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     code = models.CharField(max_length=6)
#     created_at = models.DateTimeField(auto_now_add=True)

#     @staticmethod
#     def generate_code():
#         while True:
#             code = str(random.randint(100000, 999999))
#             if not ConfirmationCode.objects.filter(code=code).exists():
#                 return code
#     def is_expired(self):
#         return timezone.now()> self.created_at + timezone.timedelta(minutes=10)

# import random
# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone
# class ConfirmationCode(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     code = models.CharField(max_length=6)
#     create_at = models.DateTimeField(auto_now_add=True)

#     @staticmethod
#     def generate_code():
#         code = str(random.randint(100000, 999999))
#         if not ConfirmationCode.objects.filter(code=code).exists():
#             return code
#     def is_expired(self):
#         return timezone.now() > self.create_at + timezone.timedelta(minutes=10)

# import random  # Импортируем модуль для генерации случайных чисел
# from django.db import models  # Импортируем классы Django для работы с моделями
# from django.contrib.auth.models import User  # Импортируем модель User из Django для связывания с пользователем
# from django.utils import timezone  # Импортируем утилиты для работы с временем (с учётом часовых поясов)

# class ConfirmationCode(models.Model):
#     # Связь с пользователем: каждый код подтверждения относится только к одному пользователю
#     user = models.OneToOneField(User, on_delete=models.CASCADE)  # Устанавливаем связь "один к одному" с пользователем
#     code = models.CharField(max_length=6)  # Поле для хранения 6-значного кода подтверждения
#     created_at = models.DateTimeField(auto_now_add=True)  # Время создания записи (автоматически сохраняется при создании)

#     def __str__(self):
#         # Метод для строкового представления объекта (например, в админке Django)
#         return f"{self.user.username} - {self.code}"  # Возвращаем строку с именем пользователя и его кодом

#     @staticmethod
#     def generate_code():
#         """
#         Генерация уникального кода подтверждения (6 цифр), который не повторяется в базе данных.
#         """
#         while True:
#             # Генерируем случайное 6-значное число
#             code = str(random.randint(100000, 999999))
#             # Проверяем, не существует ли уже такой код в базе данных
#             if not ConfirmationCode.objects.filter(code=code).exists():
#                 # Если код уникален, возвращаем его
#                 return code

#     def is_expired(self):
#         """
#         Проверка, истек ли срок действия кода.
#         Код действителен только в течение 10 минут после его создания.
#         """
#         # Если текущее время больше времени создания кода + 10 минут, код считается просроченным
#         return timezone.now() > self.created_at + timezone.timedelta(minutes=10)
