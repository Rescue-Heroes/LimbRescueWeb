#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

class PPGForm(forms.Form):
   name = forms.CharField(max_length=100)
   ppgdata = forms.FileField()
