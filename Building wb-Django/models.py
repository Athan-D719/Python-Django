
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)

    #EQUIVALENT TO:
'''
    CREATE TABLE Users(
        name VARCHAR(128),
        email VARCHAR(128)
    );     
'''