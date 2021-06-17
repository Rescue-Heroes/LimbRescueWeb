#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render

from .forms import PPGForm
from .models import PPG
from .utils import plot

def SavePPG(request):
   saved = False
   message = ""
   plot_html = "abcde"

   if request.method == "POST":
      MyPPGForm = PPGForm(request.POST, request.FILES)

      # print(request.FILES)
      # print(MyPPGForm.is_valid())

      if MyPPGForm.is_valid():
         ppg = PPG()
         ppg.name = MyPPGForm.cleaned_data["name"]
         ppg.ppgdata = MyPPGForm.cleaned_data["ppgdata"]
         if ppg.ppgdata.name.split(".")[-1].lower() == "csv":
            ppg.save()
            saved = True
            plot_html = plot(ppg.ppgdata.path)
         else:
            message = "Not .csv file. "
   else:
      MyPPGForm = PPGForm()
      message = "Failed. "

   return render(request, 'saved.html', locals())
