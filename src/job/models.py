from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.text import slugify

JOB_TYPE =(
    ('Part_Time','Part_Time'),
    ('Full_Time','Full_Time'),
)
def image_upload(instance,filename):
    image_name , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)
class job(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User,related_name="job_owner",on_delete=models.CASCADE)
    #location
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug  = models.SlugField(blank=True,null=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)  #logic
        super(job, self).save(*args,**kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name



class Apply(models.Model):
    job = models.ForeignKey(job, related_name="apply_job",on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    website = models.URLField(max_length=120)
    cv = models.FileField(upload_to="files")
    cover_letter = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name





