from django.db import models
from time import time
from django.contrib.auth.models import User


def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateField('date published')
    likes = models.IntegerField(default=0)
    thumbnail = models.FileField(upload_to=get_upload_file_name)
    is_private = models.BooleanField('Private', help_text='tick if Private', default= False)
    user= models.ForeignKey(User)
    def __unicode__(self):
        return self.title
