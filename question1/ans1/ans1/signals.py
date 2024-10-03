# create django signal to connect a receiver function

from django.dispatch import Signal, receiver

# Define a custom signal
signal1 = Signal()

# Connect the receiver to the signal
@receiver(signal1)
def receiver(sender, **kwargs):
    print("Signal received")
   
