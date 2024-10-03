from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from apps.models import Product, Category


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name', 'last_name', 'username', 'email', 'password')

    def validate(self, attrs):
        password = attrs.get('password')
        return make_password(password)

    def validate_password(self, data):
        pass


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', )


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at')


# class ProductListSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=25)
#     price = serializers.IntegerField()



class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', 'id', 'slug', 'image')

    def validate(self, attrs):
        # print(attrs)
        name = attrs.get('name', None)
        # print(name)
        if name.isdigit():
            # print("Hello")
            raise serializers.ValidationError('Not a valid product')

        return attrs


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'name',


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('created_at', 'updated_at')



