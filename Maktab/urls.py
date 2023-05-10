from django.contrib import admin
from django.urls import path
from asosiy.views import *

from django.conf import settings
from django.conf.urls.static import static

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
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
