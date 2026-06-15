from django.urls import path
from .views import TimerListCreateView, TimerDetailView

urlpatterns = [
    path('', TimerListCreateView.as_view(), name='timer-list'),
    path('<int:pk>/', TimerDetailView.as_view(), name='timer-detail'),
]