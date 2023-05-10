from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('bosh_sahifa/', bosh_sahifa),
    path('yangiliklar/', yangiliklar),
    path('media/', maktab_hayoti),
    path('jurnal/', journal),
    path('jurnalitem/', journalitems),
    path('statistika/', statistika),
    path('puplis/', puplis),
    path('contact/', contact),
]
