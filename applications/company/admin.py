from django.contrib import admin
from .models import Company, CompanyUser

@admin.register(Company)
class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ['id']


# Register your models here.
admin.site.register(CompanyUser)
# admin.site.register(AuthorAdmin)
