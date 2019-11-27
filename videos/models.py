from django.db import models

# Create your models here.
class Video(models.Model):
	CATEGORY_CHOICES = [
					(1, 'HTML/CSS'),
					(2, 'Javascript'),
					(3, 'Python'),
					(4, 'Django'),
					(5, 'Java'),
					(6, 'Asp.net'),
					(7, 'C#.net'),
					(8, 'PHP'),
					(9, 'MySQL'),
					(10, 'MongoDB'),
					(11, 'PostgreSQL')

	]
	SKILL_LEVEL_CHOICES = [
		(1, 'Beginner'),
		(2, 'Intermediate'),
		(3, 'Advanced'),
	]
	"""docstring for Video"""
	title = models.CharField(max_length = 128, unique = True)
	author = models.CharField(max_length = 64)
	description = models.TextField(blank = True, null = True)
	youtube_vid = models.CharField(max_length = 11)
	stars_count = models.DecimalField(max_digits = 2, decimal_places = 1)
	category_id = models.IntegerField(choices = CATEGORY_CHOICES)
	skill_level_id = models.IntegerField(choices = SKILL_LEVEL_CHOICES)
	is_active = models.BooleanField(default = True)
	date_posted = models.DateTimeField(auto_now_add = True)
	last_updated = models.DateTimeField(auto_now = True)


	class Meta:
		ordering = ["-stars_count","title"]

	def __str__(self):
		return self.title +'(' +self.author +')'