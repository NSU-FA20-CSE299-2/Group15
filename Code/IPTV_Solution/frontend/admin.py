from django.contrib import admin

# Register your models here.

from .models import Channel, Customer

admin.site.register(Customer)
admin.site.register(Channel)

