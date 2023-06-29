from typing import Any, List, Optional, Tuple
from urllib import request 
from django.contrib import admin ,messages 
from django.db.models.query import QuerySet 
from django.utils.html import format_html
from accounts import models
from .models import Job,Categroy



            
    
class JobsAdmin(admin.ModelAdmin):
    actions= ['clear_jobssss']
    list_per_page=10 # to make  pagentiob page
    list_filter =['title', 'published_at',]
    list_display=['title', 'categroy','salary','published_at']
    list_editable=['categroy',] # to make editing
    list_select_related = ['categroy']
    ordering=['title'] # to make sorting
    search_fields = ['title__istartswith', 'salary__istartswith'] #! to make search 
    
    
        
     #! to make filtering  and add to list_filter
    # class InventoryFilter (admin.SimpleListFilter):
    #     title = 'jobs'
    #     parameter_name = 'title'
        
    #     def lookups(self, request, model_admin): 
    #         return [
    #             ( '<1','Flutter',)
    #         ]  
    #     def queryset(self, request,queryset =QuerySet) :
    #         if self.value() == '<1':
#            return queryset.filter('Flutter__lt=1')
    #! this method is make Action to Delete a Job  and Add it actions to JobsAdmin
    # @admin.action(description = 'Clrea')
    # def clear_job(self,requset, queryset):
    #     update_count = queryset.update(job=0)
    #     self.message_user(
    #         request,
    #         f'{update_count} updateddddddddd',
    #         messages.ERROR
           
    #     )

    #! this function to make url 
    # from django.utils.html import format_html
    #    def name(self, name):
    #   return format_html('<a href="http://google.com">{} </a>', name)

    
admin.site.site_header = "Job Board with Admin"
admin.site.index_title = " Admin"

admin.site.register(Job,JobsAdmin)
admin.site.register(Categroy)




