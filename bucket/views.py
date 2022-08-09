
from rest_framework import generics,status
from rest_framework.response import Response

from bucket.script import update_models
from .serializers import BasketSerializer,Basket, DasboardSerializer, DatesSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from .models import Dashboard
import datetime

class BasketItemCreateListAPIView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BasketSerializer
    
    def get_queryset(self):
        return  Basket.objects.filter(user = self.request.user)

    def post(self, request, *args, **kwargs):
        try:
            dashboard_obj, _ = Dashboard.objects.get_or_create(user = request.user, date= datetime.date.today())
            dashboard_obj.expanse += int(request.data.get('price'))
            if request.user.userdata.total_expense<dashboard_obj.expanse:
                return Response({'message':'Cannot add item! You are going out of your salary. You may have to take a loan'},status=status.HTTP_403_FORBIDDEN)
            response = super().post(request, *args, **kwargs)
            dashboard_obj.net_amount -= response.data['price']
            dashboard_obj.save()
            return response
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    # def post(self, request, *args, **kwargs):
    #     if isinstance(request.data,dict):
    #         return super().post(request, *args, **kwargs)
        
    #     elif isinstance(request.data, list):
    #         serialized_obj = self.serializer_class(data=request.data, many=True)
    #         serialized_obj.is_valid(raise_exception=True)
    #         return Response(serialized_obj.data,status=status.HTTP_201_CREATED)

    #     else: return Response(status=status.HTTP_400_BAD_REQUEST)

class BasketUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BasketSerializer
    queryset = Basket.objects.all()

    def delete(self, request, *args, **kwargs):
        dashboard_obj, _ = Dashboard.objects.get_or_create(user = request.user, date= datetime.date.today())
        data = Basket.objects.filter(pk = kwargs['pk'])
        if data.exists():
            dashboard_obj.expanse -= data[0].price
            dashboard_obj.net_amount += data[0].price
            dashboard_obj.save()
        return super().delete(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        data = Basket.objects.filter(pk = kwargs['pk'])
        dashboard_obj, _ = Dashboard.objects.get_or_create(user = request.user, date= datetime.date.today())
        if data.exists():
            dashboard_obj.expanse -= data[0].price
            dashboard_obj.net_amount += data[0].price
            dashboard_obj.save()
        
        response = super().put(request, *args, **kwargs)
        dashboard_obj.expanse += response.data['price']
        dashboard_obj.net_amount -= response.data['price']
        dashboard_obj.save()
        return response


class FilterBasketByDate(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self,date,user):
        return Basket.objects.filter(date=date, user=user)

    def get(self,request,date):
        queryset = self.get_queryset(date,request.user)
        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serialized_obj = BasketSerializer(queryset,many = True)
        return Response(serialized_obj.data, status= status.HTTP_200_OK)

class GetAllBasketsDates(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self,user):
        return Basket.objects.filter(user=user).values('date').annotate(count = Count('date'))
    
    def get(self,request):
        queryset = self.get_queryset(request.user)
        print(queryset)
        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serialized_obj = DatesSerializer(queryset,many = True)
        return Response( serialized_obj.data,status= status.HTTP_200_OK)

class DashboardAPIView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = DasboardSerializer
    def get_queryset(self, user, date):
        if date == datetime.date.today():
            dashboard_obj, _ = Dashboard.objects.get_or_create(user = user, date= date)
        else:
            try:
                dashboard_obj= Dashboard.objects.get(user = user, date= date)
            except:
                dashboard_obj = None
        return dashboard_obj

    def get(self, request, date):
        try:
            data = self.get_queryset(request.user, date)
            serializer_obj = self.serializer_class(data)
            return Response(serializer_obj.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
    
class SearchBucketItemsAPIView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self,user,date=None,item_name=None):
        data = Basket.objects.filter(user = user)
        if date:
            data = data.filter(date = date)
        if item_name:
            data = data.filter(item__istartswith= item_name)
        if data or item_name:
            return data
        return []

    def get(self,request):
        try:
            data = self.get_queryset(user=request.user,date=request.GET.get('date'), item_name=request.GET.get('item'))
            serializer_obj = BasketSerializer(data,many = True)
            return Response(serializer_obj.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class PeriodicTaskPerDay(generics.GenericAPIView):
    def get(self,request):
        update_models()
        return Response()