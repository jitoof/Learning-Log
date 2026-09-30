from django.db import models
from django.contrib.auth.models import User
#Crea nuestros modelos aqui

class Topic(models.Model):
	"""Un tema sobre el que esta aprendiendo el usuario"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner =models.ForeignKey(User, on_delete=models.CASCADE)

	public = models.BooleanField(default=False)

	def __str__(self):
		"""Devuelve una representacion del modelo como cadena"""
		return self.text

class Entry(models.Model):
	"""Algo especifico aprendido sobre un tema"""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""Devuelve una representacion del modelo como cadena"""
		if len(self.text) > 50:
			return(f"{self.text[:50]}...")
		else: 
			return(self.text[:50])