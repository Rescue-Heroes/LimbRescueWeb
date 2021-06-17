from django.db import models
from django.contrib.auth.models import User
from .utils import OverwriteStorage


class User(models.Model):
    gender = (
        ('male', "Male"),
        ('female', "Female"),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='male')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Username'
        verbose_name_plural = 'Username'


def get_user_path(instance, filename):
    name = instance.name
    date = instance.uploaded_time.strftime("%Y-%m-%d-%H-%M")
    return f"ppgdatafile/{name}/{name}-{date}.csv"


class PPG(models.Model):
    name = models.CharField(max_length=50)
    uploaded_time = models.DateTimeField(auto_now_add=True)
    ppgdata = models.FileField(upload_to=get_user_path, storage=OverwriteStorage())

    class Meta:
        db_table = "ppg"
