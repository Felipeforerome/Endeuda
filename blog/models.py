from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	tag_choices = (
		('almargen', 'Al Margen'),
		('cyt', 'Ciencia y Tecnologia'),
		('cnv', 'Como Nos Ven'),
		('econoinf', 'Econoinformal'),
		('editorial', 'Editorial'),
		('elbobo', 'El Bobo'),
		('elintruso', 'El Intruso'),
		('elw', 'El W'),
		('endebate', 'En Deb(A)te'),
		('exogeno', 'Exogeno'),
		('opinion', 'Opinion'),
		('personajes', 'Personajes'),
		)
	title = models.CharField(max_length = 140)
	author = models.CharField(max_length = 50)
	tag = models.CharField(max_length=100, choices=tag_choices, default='')
	description = models.CharField(max_length = 280)
	body = models.TextField()
	photo = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True)
	source_of_the_photo = models.TextField(blank=False, default='')
	date = models.DateTimeField()
	promoted = models.BooleanField(default='False')

	def __unicode__(self):
		return self.title
