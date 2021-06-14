#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

from .utils import OverwriteStorage

def get_user_path(instance, filename):
   name = instance.name
   date = instance.uploaded_time.strftime("%Y-%m-%d-%H-%M")
   return f"ppgdatafile/{name}/{name}-{date}.csv"

class PPG(models.Model):
   name = models.CharField(max_length=50)
   uploaded_time = models.DateTimeField(auto_now_add=True)
   ppgdata = models.FileField(upload_to=get_user_path, storage=OverwriteStorage())

   # class Meta:
   #    db_table = "ppg"

