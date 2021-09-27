from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'middle_name', 'email_address', 'country', 'get_image')
    readonly_fields = ('get_image',)
    search_fields = ('last_name', 'email_address')

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.profile_pic.url} width=60 height=70>")
    
    get_image.short_description = 'Фото профиля'


    