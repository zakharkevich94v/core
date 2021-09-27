from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Vacancy, GeneralPageInformation


@admin.register(GeneralPageInformation)
class GeneralPageInformationAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.company_icon.url} width=80 height=70>")
    
    get_image.short_description = 'Логотип компании'


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['job_title']
    search_fields = ['job_title']
