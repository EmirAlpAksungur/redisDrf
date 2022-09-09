from rest_framework import serializers

from .models import redistodo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = redistodo
        fields = '__all__'