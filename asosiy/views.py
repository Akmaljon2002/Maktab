from django.shortcuts import render, redirect
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

class MediaView(View):
    def get(self, request):
        data = {
            'medialar': MaktabMedia.objects.all()
        }
        return render(request, 'media.html', data)

class HomeView(View):
    def get(self, request):
        data = {
            "songgilari": Yangiliklar.objects.order_by('-sana')[:4],
            'malumotlar': Malumot.objects.all()
        }
        return render(request, 'index.html', data)


class ContactView(View):
    def get(self, request):
        return render(request, 'Contact.html')

    def post(self, request):
        Murojat.objects.create(
            ism = request.POST.get('name'),
            email = request.POST.get('email'),
            tel = request.POST.get('phone'),
            sarlavha = request.POST.get('subject'),
            xabar = request.POST.get('message')
        )
        return redirect('/contact/')

