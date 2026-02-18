from django.db import models
from accounts.models import Account
from django.conf import settings



class EmailSupport(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

 

