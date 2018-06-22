from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class home(request):
    return render(request, 'index.html')


class about(request):
    return render(request, 'about.html')