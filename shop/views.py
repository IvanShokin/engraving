from django.shortcuts import render
from django.http import HttpResponse


def general(request):
    return HttpResponse('<H5>def general</H5>')


def shop(request):
    return HttpResponse('<H5>def shop</H5>')
