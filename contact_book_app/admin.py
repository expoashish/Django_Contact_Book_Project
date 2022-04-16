from django.contrib import admin

# Register your models here.
from .models import ContactDetail
from .models import *

admin.site.register(ContactDetail)
admin.site.register(ContactMessage)