from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 처음 저장할 때만 시간 저장
    updated_at = models.DateTimeField(auto_now=True) # 업데이트 할 때마다 시간 저장