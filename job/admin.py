from django.contrib import admin

from .models import Job,Categroy

class JobsAdmin(admin.ModelAdmin):
    list_display=['title', 'categroy','salary']
    list_editable=['categroy', 'salary']
    ordering=['title']
    list_per_page=10
    
admin.site.site_header = "Job Board with Admin"
admin.site.index_title = " Admin"

admin.site.register(Job,JobsAdmin)
admin.site.register(Categroy)
