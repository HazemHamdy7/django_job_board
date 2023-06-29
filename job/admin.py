from django.contrib import admin

from .models import Job,Categroy

admin.site.site_header = "Job Board with Admin"
admin.site.index_title = " Admin"

admin.site.register(Job)
admin.site.register(Categroy)
