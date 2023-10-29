from django.contrib import admin
from .models import branch1, branch2, branch3, prof
from django.contrib.auth.admin import UserAdmin
# from .models import User

# admin.site.register(User, UserAdmin)

admin.site.register(branch1)
admin.site.register(branch2)
admin.site.register(branch3)
admin.site.register(prof)
# Register your models here.
