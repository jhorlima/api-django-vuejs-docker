from rest_framework import viewsets
from .models import Consumer
from .serializers import ConsumerSerializer

# Create your views here.
# ViewSets define the view behavior.
class ConsumerViewSet(viewsets.ModelViewSet):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer