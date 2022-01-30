from django.contrib import admin
from .models import profile


class profileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'state_of_origin', 'date_of_birth')


# Register your models here.
admin.site.register(profile, profileAdmin)

