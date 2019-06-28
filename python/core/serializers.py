from rest_framework import serializers
from .models import Consumer

# Serializers define the API representation.
class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = ('id', 'name', 'address', 'age')
