from django.contrib import admin

# Register your models here.
from .models import List

#admin.site.register(Form)

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'created', 'modified')