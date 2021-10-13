from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from django.http import HttpResponse



@api_view(["GET"])
def myview(hello):
    return HttpResponse("good morning")
