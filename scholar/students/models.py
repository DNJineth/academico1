from django.db import models
from django.utils import timezone
import datetime
class User(models.Model):
<<<<<<< HEAD
    email = models.CharField (max_length = 100 , null = False)
    password = models.CharField (max_length = 500, null = False )
    status = models.BooleanField (default = True, null = True)
    create_at = models.DateTimeField (default = datetime.datetime.now, null = False)
    updated_at = models.DateTimeField (default = datetime.datetime.now, null = False)
    deleted_at = models.DateTimeField (null = True)
=======
    email = models.CharField (max_length = 100)
    password = models.CharField (max_length = 500)
    dni= models.CharField (max_length = 10, default = '') 
    age= models.IntegerField (default = 0)
    
>>>>>>> d048d99e1ef798ced7e46b13dd251dde61f93ab6
    
# Create your models here.
class   Persons(models.Model):
    id- = models.IntField (null = False )
    last_name = models.CharField (max_length = 50, null = False )
    id_ident_type = models.IntField (null = False )
    status = models.BooleanField (default = True, null = True)
    create_at = models.DateTimeField (default = datetime.datetime.now, null = False)
    updated_at = models.DateTimeField (default = datetime.datetime.now, null = False)
    deleted_at = models.DateTimeField (null = True)
    
    