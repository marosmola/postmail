import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Client(models.Model):
    name = models.CharField('Názov', max_length=100, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Client, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Klient'
        verbose_name_plural = 'Klienti'


class PostmarkIntegration(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField()
    postmark_api_token = models.CharField(max_length=100)
    from_email = models.EmailField()
    to_emails = models.CharField(max_length=255)

    def __str__(self):
        return "postmark_{}".format(self.token)

    class Meta:
        verbose_name = 'Postmark integrácia'
        verbose_name_plural = 'Postmark integrácie'
