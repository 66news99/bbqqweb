from django.db import models

# Create your models here.


class NewModel(models.Model):   # 모델즈 안에 모델
    text = models.CharField(max_length=255, null=False)  # CharField 문자필드?/null=false는 무조건 넣는단 말
