

from django.http import HttpResponse
from .signals import signal1

def trigger_signal(request):
    print("View executed")
    
    # Send the signal
    signal1.send(sender=None)
    
    print("View executed successfully")
    
    return HttpResponse("Signal triggered.")
