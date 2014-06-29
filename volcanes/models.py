from django.db import models

# Create your models here.
class Volcan(models.Model):
	nombre = models.CharField(max_length=25)
	altura = models.PositiveIntegerField()
	imagen = models.Fileield(upload_to='cargas/')
	descripcion = models.TextField()
	def __unicode__(self):
		return self.nombre