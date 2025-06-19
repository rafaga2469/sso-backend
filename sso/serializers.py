from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "email", "password", "confirm_password")

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"password": "Las contraseñas no coinciden."})
        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        return user
