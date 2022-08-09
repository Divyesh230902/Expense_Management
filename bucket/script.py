import datetime
from .models import Dashboard
from django.contrib.auth.models import User

today = datetime.date.today()
yesterday =  today - datetime.timedelta(1)

users = User.objects.all()

dashb = Dashboard.objects

def update_today( yesterday_obj, user):
    userdata = user.userdata
    userdata.expense += (-yesterday_obj.net_amount)
    userdata.save()
    

def update_models():
    today = datetime.date.today()
    yesterday =  today - datetime.timedelta(1)

    users = User.objects.all()

    dashb = Dashboard.objects

    for user in users:
        if dashb.filter(user = user, date = yesterday).exists():
            update_today(dashb.get(user=user, date = yesterday), user)
