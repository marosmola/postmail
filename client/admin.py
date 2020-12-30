from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Client, PostmarkIntegration


class PostmarkIntegrationAdmin(admin.ModelAdmin):
    readonly_fields = ('token',)

admin.site.register(User, UserAdmin)
admin.site.register(Client)
admin.site.register(PostmarkIntegration, PostmarkIntegrationAdmin)
