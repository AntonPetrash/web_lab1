from rest_framework import serializers
from .models import Timer

class TimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer
        fields = ['id', 'user', 'name', 'start_time', 'end_time', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']