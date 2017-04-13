# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
from generic.models import BaseModel



class Category(BaseModel):
	category = models.CharField(max_length=128)
	slug = models.SlugField(max_length=128, unique=True)



	class Meta:
		db_table = "categories"

	def __unicode__(self):
		return self.category


	# def save()


class Product(BaseModel):
	category = models.ManyToManyField("product.category")
	product = models.CharField(max_length=128)
	slug = models.SlugField(max_length=128, unique=True)

	class Meta:
		db_table = "products"

	def __unicode__(self):
		return self.product