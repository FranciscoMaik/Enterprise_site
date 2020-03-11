from django.shortcuts import render
from .models import noticias, profissionais
from django.utils import timezone

def noticias_jua(request):
    information = noticias.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'site_empresa_jua/noticias_jua.html', {'information': information})


# Create your views here.
