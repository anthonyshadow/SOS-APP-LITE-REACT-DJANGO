from django.contrib import admin
from .models import User

class PacksterAdmin(admin.ModelAdmin):
    user_display = ('name', 'email', 'age')

# Register your models here.
admin.site.register(User, PacksterAdmin)