from django.db import models

class Text(models.Model):
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    #writer = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='작성자')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

# Create your models here.
