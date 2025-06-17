from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot_ui, name='chat_ui'),
    path('api/', views.chat_response, name='chat_api'),
]
