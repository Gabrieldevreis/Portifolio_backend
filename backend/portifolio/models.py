from django.db import models

# Create your models here.
'''title: string;
  description: string;
  image: string;
  alt: string;
  techs: string[];
  demoLink: string;
  codeLink: string;'''

class Techs(models.Model):
    id= models.AutoField(primary_key=True, editable=False)
    name= models.CharField(max_length=50)

    def __str__ (self):
        return self.name

class Projects(models.Model):
    id= models.AutoField(primary_key=True,editable=False)
    title= models.CharField(max_length=100)
    description= models.TextField()
    image= models.ImageField(upload_to='images/')
    alt= models.CharField(blank=True,null=True)
    techs= models.ManyToManyField(Techs,related_name='projects')
    demo_link= models.CharField(blank=True,null=True)
    code_link= models.CharField(blank=True,null=True)
    uptade_at= models.DateTimeField(auto_now=True)
    create_at= models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.title
    


    



