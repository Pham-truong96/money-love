from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class BaseModel(models.Model):
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(__class__, self).save(*args, **kwargs)
    
    class Meta:
        abstract = True 


class Transaction(BaseModel):
    name = models.CharField(max_length=200)
    desc = models.TextField(null=True)
    price = models.BigIntegerField()
    
    class Meta:
        db_table = 'transaction'
    

class Invoice(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, db_column='transaction_id')
    complete = models.BooleanField(default=False)

    class Meta:
        db_table = 'invoice' 
