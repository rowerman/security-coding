from django.contrib import admin
from .models import UserProfile,UserInfo
from django.forms import TextInput, Textarea
from django.db import models


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','birth','phone')
    list_filter = ("phone",)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("user",'school','company','profession','address','aboutme','photo')
    list_filter = ("school","company","profession")
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(UserInfo,UserInfoAdmin)