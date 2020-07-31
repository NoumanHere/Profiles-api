from rest_framework import serializers
from .models import UserProfile


class HelloSerialize(serializers.Serializer):
    """Serializers a name field for testing my api view."""
    name = serializers.CharField(max_length = 10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    
    class Meta:
        model = UserProfile
        fields = ('id,email,name,password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{
                    'input_type':'password'
                }
            }
        }
    
    def create(self, validated_data):
        """Create and return new user"""
        user = UserProfile.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        
        return user