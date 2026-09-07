from django.contrib import admin
from .models import ContactMessage, Project, Certificate


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "project_type", "created_at")
    search_fields = ("name", "project_type", "technologies")
    ordering = ("-created_at",)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("title", "issuer", "issue_date")
    search_fields = ("title", "issuer")
    ordering = ("-id",)