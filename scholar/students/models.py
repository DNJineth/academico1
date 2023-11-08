from django.db import models
from django.utils import timezone
import datetime
class User(models.Model):
    email = models.CharField (max_length = 100 , null = False)
    password = models.CharField (max_length = 500, null = False )
    status = models.BooleanField (default = True, null = True)
    create_at = models.DateTimeField (default = datetime.datetime.now, null = False)
    updated_at = models.DateTimeField (default = datetime.datetime.now, null = False)
    deleted_at = models.DateTimeField (null = True)
    
# Create your models here.
class   Persons(models.Model):
    id- = models.IntField (null = False )
    last_name = models.CharField (max_length = 50, null = False )
    id_ident_type = models.IntField (null = False )
    status = models.BooleanField (default = True, null = True)
    create_at = models.DateTimeField (default = datetime.datetime.now, null = False)
    updated_at = models.DateTimeField (default = datetime.datetime.now, null = False)
    deleted_at = models.DateTimeField (null = True)
    
    