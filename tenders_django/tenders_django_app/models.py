# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Tender(models.Model):
    Tender_Notice_Type = models.CharField(max_length=250)
    Country = models.CharField(max_length=250)
    Category = models.CharField(max_length=250)
    Description = models.CharField(max_length=250)
    Deadline = models.CharField(max_length=250)
    Ref = models.CharField(max_length=250)
    classification = models.CharField(max_length=100)
