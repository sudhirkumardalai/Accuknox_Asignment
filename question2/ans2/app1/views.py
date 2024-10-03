# myproject/views.py
from django.http import HttpResponse
from .models import MyModel

def create_model(request):
    obj = MyModel(name='Test')
    obj.save()  # This will trigger the post_save signal
    return HttpResponse("Model created!")
