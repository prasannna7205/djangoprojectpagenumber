from django.shortcuts import render
from pagenumberapp.models import Addpagelist
from pagenumberapp.serializers import AddSeralizer
from django.views.generic import View
from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from pagenumberapp.pagenation import Mypaginations
# Create your views here.
class Getview(ListAPIView):
    queryset = Addpagelist.objects.all()
    serializer_class = AddSeralizer  # Correct the typo here
    pagination_class = Mypaginations

