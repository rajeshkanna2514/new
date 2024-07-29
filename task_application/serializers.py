from rest_framework import serializers


from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from .models import User,TaskModel

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50,min_length=6,write_only=True)
    class Meta:
        model = User
        fields = ('username','email','password')

        extra_kwargs = {
            'password':{'write_only':True}
        }


   
    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')

        if not username.isalnum():  # isalnum is only for num and char not useSpecialChar
            raise serializers.ValidationError("Incorrect Username or Email")
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=50, min_length=3)
    password = serializers.CharField(max_length=50, min_length=6,write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            raise AuthenticationFailed("email and password are required")

        user = authenticate(email=email, password=password)
        # if not user:
        #     raise AuthenticationFailed("Invalid login credentials")
        
        data['user'] = user
        return data

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'