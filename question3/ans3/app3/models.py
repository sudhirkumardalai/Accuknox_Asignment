from django.db import models
from django.db.models.signals import post_save
from django.db import transaction

class Book(models.Model):
    title = models.CharField(max_length=255)

# Signal handler
def signal_update_title(sender, instance, **kwargs):
    # Modify the title inside the signal
    instance.title = instance.title + " - updated by signal"
    instance.save()

post_save.connect(signal_update_title, sender=Book)
