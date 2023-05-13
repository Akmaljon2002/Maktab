from django.contrib import admin
from django.urls import path
from asosiy.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('news/', YangiliklarView.as_view()),
    path('news2/', Yangiliklar2View.as_view()),
    path('new/<int:pk>/', YangilikDetailView.as_view()),

    path('media/', MediaView.as_view()),
    path('stats/room/', StatsRoomView.as_view()),
    path('stats/puplis/', StatsPuplisView.as_view()),
    path('media2/', Media2View.as_view()),
    path('contact/', ContactView.as_view()),
    path('contact2/', Contact2View.as_view()),
    # path('journal/', JournalView.as_view()),
    path('journal/<int:pk>/', JournalSinfView.as_view()),
    path('journalitems/', JournalItemsView.as_view()),
    path('home/', Home2View.as_view()),
    path('logout/', LogoutView.as_view()),
    path('', HomeView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
