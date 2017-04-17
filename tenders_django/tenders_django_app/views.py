# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView
from tenders_django_app.models import Tender
# Create your views here.

class TendersView(ListView):
    template_name = "tenders.html"
    model = Tender

    def get_context_data(self, **kwargs):
        context = super(TendersView, self).get_context_data(**kwargs)
        context['Tenders'] = Tender.objects.all()
        return context
