from django.db import models
from django.utils import timezone

class Post(models.Model):
	autor=models.ForeignKey('auth.User')
	titulo=models.CharField(max_length=200)
	texto=models.TextField()
	fecha_creacion=models.DateTimeField(default=timezone.now)
	fecha_publicacion=models.DateTimeField(blank=True, null=True)

def publicar(self):
	self.fecha_publicacion=timezone.now()
	self.save()

def _str_(self):
	return self.titulo 

# Create your models here.
