from django.shortcuts import render

def bosh_sahifa(request):
    return render(request, 'index.html')

def yangiliklar(request):
    return render(request, 'news.html')

def maktab_hayoti(request):
    return render(request, 'media.html')

def journal(request):
    return render(request, 'journal.html')

def journalitems(request):
    return render(request, 'journalItems.html')

def statistika(request):
    return render(request, 'Statistics/Room.html')

def puplis(request):
    return render(request, 'Statistics/puplis.html')

def contact(request):
    return render(request, 'Contact.html')