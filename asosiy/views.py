from django.shortcuts import render
from django.views import View
from .models import *

class YangiliklarView(View):
    def get(self, request):
        data = {
            'yangiliklar':Yangiliklar.objects.all()
        }
        return render(request, 'news.html', data)

class YangilikDetailView(View):
    def get(self, request, pk):
        data = {
            "yangilik":Yangiliklar.objects.get(id=pk)
        }
        return render(request, 'newsTitle.html', data)