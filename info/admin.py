from django.contrib import admin
from info.models import *
# Register your models here.
admin.autodiscover()

class StudentAdmin(admin.ModelAdmin):
    list_display= ( 'name' , 'roll_no' )
    
    
admin.site.register(Student, StudentAdmin)
