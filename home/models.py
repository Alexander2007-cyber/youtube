from django.db import models
import random
import string

def generate_unique_code():
    length = 12
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if AddedVideo.objects.filter(code=code).count() == 0:
            break

    return code

class AddedVideo(models.Model):
    code = models.CharField(max_length=12, default=generate_unique_code, unique=True, null=True)
    title = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='video')