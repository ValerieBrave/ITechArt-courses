from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from .models import PhoneCatalog


def index(request):
    message = None
    if "message" in request.GET:
        message = request.GET["message"]
    return render(
        request,
        "index.html",
        {
            "latest_phones":
                PhoneCatalog.objects.order_by('-reg_date')[:5],
            "message": message
        }
    )

# Create your views here.
