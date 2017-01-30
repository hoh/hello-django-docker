from django.contrib import admin
from .models import DatabaseObject


class DatabaseObjectAdmin(admin.ModelAdmin):
    fields = ('name',)


admin.site.register(DatabaseObject, DatabaseObjectAdmin)
