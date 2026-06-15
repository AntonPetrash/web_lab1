from rest_framework import generics, permissions
from .models import Timer
from .serializers import TimerSerializer


class TimerListCreateView(generics.ListCreateAPIView):
    serializer_class = TimerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Timer.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TimerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TimerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Timer.objects.filter(user=self.request.user)