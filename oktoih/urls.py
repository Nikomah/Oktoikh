from django.urls import path
from .views import *


urlpatterns = [
    path('', main, name='home'),
    path('<int:pk>', Voices.as_view(), name='voices'),
    path('send-massage', send_message, name='message'),
    path('sunday/evang', SundayEvang.as_view(), name='evang'),
    path('sunday/exapost', SundayExapost.as_view(), name='exapost'),
    path('sunday/st-ev', SundayStEv.as_view(), name='st_ev'),
    ]
