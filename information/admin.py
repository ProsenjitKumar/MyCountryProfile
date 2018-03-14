from django.contrib import admin
from .models import Divisions, Districts

# Register your models here.

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'division', 'population_density','education_rate' ,'visited' )


admin.site.register(Divisions)
admin.site.register(Districts, DistrictAdmin)
