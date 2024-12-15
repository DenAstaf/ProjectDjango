from django.shortcuts import render

from django.http import HttpResponse


def store(request):
    return HttpResponse("Hello. This is a store.")
