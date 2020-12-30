import logging

from django.shortcuts import render
from postmarker.core import PostmarkClient
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import PostmarkIntegration

logger = logging.getLogger(__name__)


class PostEmail(APIView):
    def post(self, request, format=None):
        token = request.data.get('token', None)
        subject = request.data.get('subject', None)
        message = request.data.get('message', None)
        receiver = request.data.get('receiver', None)

        if token:
            try:
                integration = PostmarkIntegration.objects.get(token=token)
            except PostmarkIntegration.DoesNotExists:
                return Response('Integration not found', status=status.HTTP_404_NOT_FOUND)

            if integration.url != request.META.get('HTTP_ORIGIN'):
                return Response('Origin not allowed', status=status.HTTP_400_BAD_REQUEST)

            postmark = PostmarkClient(server_token=integration.postmark_api_token)
            postmark.emails.send(
                From=integration.from_email,
                To=receiver,
                Subject=subject,
                HtmlBody=message
            )

            return Response('Sent', status=status.HTTP_201_CREATED)

        return Response('Token is missing', status=status.HTTP_404_NOT_FOUND)
