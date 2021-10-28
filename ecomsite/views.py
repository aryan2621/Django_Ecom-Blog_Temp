from django.shortcuts import render
from math import ceil


def index(request):
    return render(request, "index.html")
