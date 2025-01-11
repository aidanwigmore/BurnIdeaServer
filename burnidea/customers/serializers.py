import logging
from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext_lazy as _

from .models import Customer

logger = logging.getLogger(__name__)

User = get_user_model()

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'given_name', 'phone_number', 'subscribed_to_newsletter', 'sms_notifications', 'email_notifications', 'is_staff']
        extra_kwargs = {
            'email': {'read_only': True},  # Email should not be updated
        }

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'given_name', 'password', 'phone_number', 'subscribed_to_newsletter', 'sms_notifications', 'email_notifications']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Customer.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            given_name=validated_data['given_name'],
            password=validated_data['password'],
            phone_number=validated_data['phone_number'],
            subscribed_to_newsletter=validated_data['subscribed_to_newsletter'],
            sms_notifications=validated_data['sms_notifications'],
            email_notifications=validated_data['email_notifications']
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')        
        password = data.get('password')

        logger.debug(f'Attempting to authenticate user with email: {email}')

        if email and password:
            user = authenticate(request=self.context.get('request'), username=email, password=password)
            if not user:
                logger.error(f'Authentication failed for email: {email}')
                logger.debug(f'User exists: {User.objects.filter(email=email).exists()}')
                if User.objects.filter(email=email).exists():
                    logger.debug(f'Password correct: {User.objects.get(email=email).check_password(password)}')
                raise serializers.ValidationError(_('Unable to log in with provided credentials.'), code='authorization')
        else:
            logger.error('Email and password must be provided')
            raise serializers.ValidationError(_('Must include "email" and "password".'), code='authorization')

        data['user'] = user
        return data
    