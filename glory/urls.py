from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('bartender/', BartenderView.as_view(), name='bartender'),
    path('dining/', DiningView.as_view(), name='dining'),
    path('suite/', SuiteView.as_view(), name='suite'),
    path('activities/', ActivitiesView.as_view(), name='activities'),
    path('weddings/', WeddingView.as_view(), name='weddings'),
    path('meetings/', MeetingView.as_view(), name='meetings'),
    path('room/<int:pk>/', RoomView.as_view(), name='room'),
    path('order/<int:pk>/', OrderView.as_view(), name='order-check'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
