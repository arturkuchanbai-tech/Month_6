import random
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ConfirmationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.code}"

    @staticmethod
    def generate_code():
        while True:
            code = str(random.randint(100000, 999999))
            if not ConfirmationCode.objects.filter(code=code).exists():
                return code

    def is_expired(self):
        return timezone.now() > self.created_at + timezone.timedelta(minutes=10)
    
