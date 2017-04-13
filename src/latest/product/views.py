# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from .models import Category,Product
from .forms import (
					CategoryForm,
					ProductForm, 
					CategoryFormset,
					ProductFormset
					)




def dashboard(request):
	template = "product/dashboard.html"
	context = {}

	return render(request, template, context)

