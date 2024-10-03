
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading

# Create a simple model
class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, created, **kwargs):
    # This will print the current thread's name
    print(f"Signal received in thread: {threading.current_thread().name}")
