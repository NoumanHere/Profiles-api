from rest_framework import serializers

class HelloSerialize(serializers.Serializer):
    """Serializers a name field for testing my api view."""
    name = serializers.CharField(max_length = 10)