from django.contrib import admin
from django.urls import path
from asosiy.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('news/', YangiliklarView.as_view()),
    path('new/<int:pk>/', YangilikDetailView.as_view()),

    path('media/', MediaView.as_view()),
    path('', HomeView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
