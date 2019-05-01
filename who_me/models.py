from django.db import models
from django.utils import timezone

class FaceInfo(models.Model):
    # 질문을 삭제 했을 때 연관 항목을 어떻게 할지 설정 - 자동 삭제
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    photo = models.ImageField(blank=True)
    gender = models.CharField(max_length = 20)
    age = models.IntegerField(default = 0)
    emotion = models.TextField()
    celebrity_name = models.CharField(max_length = 100)
    confidence = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)