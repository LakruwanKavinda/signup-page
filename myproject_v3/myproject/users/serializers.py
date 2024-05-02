from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Adjust fields as needed
        fields = ('id', 'username', 'email', 'password')
        # Hide password on retrieval
        extra_kwargs = {'password': {'write_only': True}}
