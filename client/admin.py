from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Client, PostmarkIntegration

import logging

logger = logging.getLogger(__name__)

class ClientAdmin(admin.ModelAdmin):
    fields = ('name',)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or (obj and obj.created_by == request.user)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(created_by=request.user)


class PostmarkIntegrationAdmin(admin.ModelAdmin):
    list_display = ('client', 'url', 'token')
    readonly_fields = ('token',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        clients = Client.objects.filter(created_by=request.user)
        return qs.filter(client__in=clients)

    def get_form(self, request, obj=None, **kwargs):
        form = super(PostmarkIntegrationAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['client'].queryset = Client.objects.filter(created_by=request.user)
        return form


admin.site.register(User, UserAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(PostmarkIntegration, PostmarkIntegrationAdmin)
