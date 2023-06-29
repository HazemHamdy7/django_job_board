from django.contrib import admin
from django.utils.html import format_html
from accounts import models
from .models import Job,Categroy


    
class JobsAdmin(admin.ModelAdmin):
    list_per_page=10 # to make  pagentiob page
    list_display=['title', 'categroy','salary',]
    list_editable=['categroy',] # to make editing
    list_select_related = ['categroy']
    ordering=['title'] # to make sorting
    search_fields = ['title__istartswith', 'salary__istartswith'] # to make search 

    
admin.site.site_header = "Job Board with Admin"
admin.site.index_title = " Admin"

admin.site.register(Job,JobsAdmin)
admin.site.register(Categroy)




#! this function to make url 
# from django.utils.html import format_html
#    def name(self, name):
#   return format_html('<a href="http://google.com">{} </a>', name)