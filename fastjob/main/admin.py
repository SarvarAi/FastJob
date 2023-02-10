from django.contrib import admin
from .models import CV, CategoryCV


class CVAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Surname', 'city', 'username', 'proffession', 'date_of_creation')
    list_display_links = ('Name', 'city')
    list_filter = ('city', 'proffession', 'date_of_creation', 'type_cv')


# Register your models here.
admin.site.register(CV, CVAdmin)
admin.site.register(CategoryCV)
