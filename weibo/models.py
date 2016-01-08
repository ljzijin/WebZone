from django.db import models

# Create your models here.
class Blog(models.Model):
	blog_user=models.IntegerField()
	blog_content=models.CharField(max_length=1024)
	created_at=models.DateTimeField(auto_now_add=True)

	class Meta(object):
		db_table='weibo_blog'