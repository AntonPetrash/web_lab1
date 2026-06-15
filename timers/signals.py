from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Timer
from .serializers import TimerSerializer


@receiver(post_save, sender=Timer)
def timer_post_save(sender, instance, created, **kwargs):
    channel_layer = get_channel_layer()
    action = 'created' if created else 'updated'
    serializer = TimerSerializer(instance)
    async_to_sync(channel_layer.group_send)(
        'timer_updates',
        {
            'type': 'send_timer_update',
            'action': action,
            'timer': serializer.data
        }
    )


@receiver(post_delete, sender=Timer)
def timer_post_delete(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'timer_updates',
        {
            'type': 'send_timer_update',
            'action': 'deleted',
            'timer': {'id': instance.id}
        }
    )