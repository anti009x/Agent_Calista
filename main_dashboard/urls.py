from django.urls import path
from . import views
from . import model_run

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('send_message/', model_run.process_message, name='send_message'),
    path('send_message_web_search/', model_run.process_message_web_search, name='send_message_web_search'),
]