from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class SignUpModelAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','profile_image','username','email','password','address']