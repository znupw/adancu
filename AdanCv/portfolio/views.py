from django.shortcuts import render
from .models import Proyecto

# Create your views here.

def portfolio(request):
    projects = Proyecto.objects.all()
    return render(request, "portfolio/portfolio.html",{'projects':projects})
