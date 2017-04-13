# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid
# Create your models here.

class BaseModel(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	created_by = models.ForeignKey("auth.User", related_name="%(class)s_created")
	modified_by = models.ForeignKey("auth.User", related_name="%(class)s_modified")
	created_on = models.DateTimeField()
	modified_on = models.DateTimeField()

	class Meta:
		abstract = True