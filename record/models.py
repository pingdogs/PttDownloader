from django.db import models

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=15, unique=True)
	url = models.URLField(default='', blank=True)

	def url_default(self):
		return 'https://www.ptt.cc/bbs/' + self.name + "/index.html"

	def save(self, *args, **kwargs):
	    self.url = self.url_default()
	    super(Category, self).save(*args, **kwargs)

	def __str__(self):
		return self.name



class KeyWord(models.Model):
	name = models.CharField(max_length=15, unique=True)
	categories = models.ManyToManyField(Category)

	def __str__(self):
		return self.name


class Article(models.Model):
	title = models.CharField(max_length=15)
	category = models.ForeignKey(Category,related_name='category_of_article', on_delete=models.PROTECT, default='')
	date = models.CharField(max_length=15)
	author = models.CharField(max_length=15)
	pushes = models.IntegerField()
	content = models.TextField(default='')

	def __str__(self):
		return self.title

	class Meta:
		constraints = [ models.UniqueConstraint(fields=['title', 'author', 'date'], name='name of constraint')]