from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(UserData)
admin.site.register(UserUpdateHistory)
admin.site.register(Notification)
