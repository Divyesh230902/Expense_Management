from django.db import models
from django.contrib.auth import get_user_model
import datetime
from django.dispatch import receiver
from django.db.models.signals import pre_save

# Create your models here.
class Basket(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='basket')
    item = models.CharField(max_length=50)
    price = models.IntegerField()
    date = models.DateField(default=datetime.date.today)

class Dashboard(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='dashboard')
    date = models.DateField()
    budget = models.BigIntegerField()
    expanse = models.BigIntegerField(default=0)
    net_amount = models.BigIntegerField()

@receiver(pre_save, sender=Dashboard)
def dasboard_init(sender,instance, **kwargs):
    if not instance.budget:
        instance.budget = instance.user.userdata.daily_budget
    if not instance.net_amount:
        instance.net_amount = instance.user.userdata.daily_budget



