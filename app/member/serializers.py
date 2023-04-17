from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "email"]
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User(
                username=validated_data['username'],
                email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(username=username, password=password)
        if user:
            attrs['user'] = user
        else:
            raise serializers.ValidationError("Authorization Error")
        
        return attrs
