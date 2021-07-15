from typing import Text
from django.db import models
import datetime

class Ticket(models.Model):
    id = models.SlugField('ID',primary_key=True,max_length=150,unique=True)
    text = models.TextField('Text',default='')
    date = models.DateField('Date',auto_now=True,auto_now_add=False)
    exp_date = models.DateField('Exp_date',auto_now=True)