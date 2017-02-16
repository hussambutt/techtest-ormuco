from django.contrib import admin

# Register your models here.
from .models import Form, List

admin.site.register(Form)

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('name',)