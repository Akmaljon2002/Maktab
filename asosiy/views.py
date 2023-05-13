from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .models import *

class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                "songgilari": Yangiliklar.objects.order_by('-sana')[:4],
                'malumotlar': Malumot.objects.all()
            }
            return render(request, 'index.html', data)
        return redirect('/home/')

class Home2View(View):
    def get(self, request):
        data = {
            "songgilari": Yangiliklar.objects.order_by('-sana')[:4],
            'malumotlar': Malumot.objects.all()
        }
        return render(request, 'Bosh_loginli.html', data)
    def post(self, request):
        user = authenticate(username= request.POST.get('l'),
                            password = request.POST.get('p'))
        if user is None:
            return redirect('/home/')
        login(request, user)
        return redirect('/')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")

class Yangiliklar2View(View):
    def get(self, request):
        data = {
            'yangiliklar':Yangiliklar.objects.all()
        }
        return render(request, 'news2.html', data)
    def post(self, request):
        user = authenticate(username= request.POST.get('l'),
                            password = request.POST.get('p'))
        if user is None:
            return redirect('/news2/')
        login(request, user)
        return redirect('/news/')

class YangiliklarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'yangiliklar':Yangiliklar.objects.all()
            }
            return render(request, 'news.html', data)
        return redirect('/news2/')

class YangilikDetailView(View):
    def get(self, request, pk):
        data = {
            "yangilik":Yangiliklar.objects.get(id=pk)
        }
        return render(request, 'newsTitle.html', data)

class MediaView(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'medialar': MaktabMedia.objects.all()
            }
            return render(request, 'media.html', data)
        return redirect('/media2/')

class Media2View(View):
    def get(self, request):
        data = {
            'medialar': MaktabMedia.objects.all()
        }
        return render(request, 'media2.html', data)
    def post(self, request):
        user = authenticate(username= request.POST.get('l'),
                            password = request.POST.get('p'))
        if user is None:
            return redirect('/media2/')
        login(request, user)
        return redirect('/media/')


class ContactView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'Contact.html')
        return redirect('/contact2/')

    def post(self, request):
        if request.user.is_authenticated:
            Murojat.objects.create(
                ism = request.POST.get('name'),
                email = request.POST.get('email'),
                tel = request.POST.get('phone'),
                sarlavha = request.POST.get('subject'),
                xabar = request.POST.get('message')
            )
            return redirect('/contact/')
        return redirect('/contact2/')

class Contact2View(View):
    def get(self, request):
        return render(request, 'Contact2.html')

    def post(self, request):
        if request.POST.get('l') is None:
            Murojat.objects.create(
                ism = request.POST.get('name'),
                email = request.POST.get('email'),
                tel = request.POST.get('phone'),
                sarlavha = request.POST.get('subject'),
                xabar = request.POST.get('message')
            )
            return redirect('/contact2/')
        else:
            user = authenticate(username=request.POST.get('l'),
                                password=request.POST.get('p'))
            if user is None:
                return redirect('/contact2/')
            login(request, user)
            return redirect('/contact/')



class StatsRoomView(View):
    def get(self, request):
        # if request.user.is_authenticated:
            return render(request, 'Statistics/Room.html')


class StatsPuplisView(View):
    def get(self, request):
        # if request.user.is_authenticated:
            return render(request, 'Statistics/puplis.html')


class JournalSinfView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            sinflar = Sinf.objects.filter(id_sinf=pk)
            for sinf in sinflar:
                fanlar = sinf.fan.all()
            data = {
                "fanlar":fanlar
            }
            return render(request, 'journal.html', data)
        return redirect('/home/')

# class JournalView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return render(request, 'journal.html')
#         return redirect('/home/')


class JournalItemsView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'journalItems.html')
        return redirect('/home/')

