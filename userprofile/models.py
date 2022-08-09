from django.db import models
from django.contrib.auth import get_user_model
import datetime, calendar

# Create your models here.
class UserData(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='userdata')
    salary = models.BigIntegerField()
    expense = models.BigIntegerField(default=0)

    def __str__(self) -> str:
        return self.user.username

    @property
    def days_in_month(self):
        today = datetime.date.today()
        total_days = calendar.monthrange(today.year,today.month)
        return total_days[1]

    @property
    def days_left(self):
        today = datetime.date.today()
        return self.days_in_month - today.day
    
    @property
    def default_saving(self):
        return self.salary*(len(str(self.salary))*2/100)

    @property
    def total_expense(self):
        return self.salary - self.default_saving - self.expense

    @property
    def daily_budget(self):
        return round(self.total_expense/self.days_left)

    @property
    def daily_saving(self):
        return round(self.default_saving/self.days_in_month)
