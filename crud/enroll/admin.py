from django.contrib import admin
from enroll.models import user
# Register your models here.

@admin.register(user)
class useramdin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')