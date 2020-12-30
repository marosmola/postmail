import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Názov', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Klient'
        verbose_name_plural = 'Klienti'


class PostmarkIntegration(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField()
    postmark_api_token = models.CharField(max_length=100)
    from_email = models.EmailField()

    def __str__(self):
        return "postmark_{}".format(self.token)

    class Meta:
        verbose_name = 'Postmark integrácia'
        verbose_name_plural = 'Postmark integrácie'
