import os
import uuid
from django.db import models

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

class Categroy(models.Model):
    name= models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

   
# def image_upload (instance,filename):
#      imagename , extension = filename.split(".")
#      return "imagejobs/%s.%s"%(isinstance.id,extension)
     
def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    new_filename = imagename + str(uuid.uuid4())[:8] + "." + extension
    return os.path.join("images/", new_filename)
   
class Job(models.Model):
    title= models.CharField(max_length=100)
    #location= models
    job_type= models.CharField(max_length=15 ,choices=JOB_TYPE)
    description= models.TextField(max_length=1000)
    published_at= models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    categroy = models.ForeignKey(Categroy,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="image_jobs")

    def __str__(self):
        return self.title
  
