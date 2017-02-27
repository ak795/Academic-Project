from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django import forms
# Create your models here.

class FormText(models.Model):
    text = models.TextField()
    label = models.CharField(max_length=200)
    sub_label = models.CharField(max_length=200)
    score_pos = models.DecimalField(decimal_places=10,max_digits=20)
    score_neg = models.DecimalField(decimal_places=10,max_digits=20)
    score_neu = models.DecimalField(decimal_places=10,max_digits=20)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()

    def __str__(self):
        return self.label





