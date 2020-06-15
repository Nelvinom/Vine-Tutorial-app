from django.db import models
import datetime as dt
from tinymce.models import HTMLField
# Create your models here.


class Tutorial(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=100, blank=True, )
    published = models.BooleanField(default=False)
    description = models.TextField(max_length = 500, blank=False, default='')
    Image = models.ImageField(upload_to='images/', default='')
    code = HTMLField(max_length=500, default='')
    owner = models.ForeignKey('auth.User', related_name='tutorials', on_delete=models.CASCADE, null=True)
    highlighted = models.TextField(max_length=50, default='')
    published
    
    def __str__(self):
        return self.title
    class meta:
        ordering =['name']
    
    def save_editor(self):
        self.save()
    @classmethod
    def search_by_title(cls,search_term):
        tutorials = cls.objects.filter(title__icontains=search_term)
        return tutorials    