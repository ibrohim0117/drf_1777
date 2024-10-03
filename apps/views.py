from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView,
    DestroyAPIView, UpdateAPIView, ListCreateAPIView,
    RetrieveUpdateDestroyAPIView, get_object_or_404
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Category
from .serializers import UserCreateSerializer, UserListSerializer, UserUpdateSerializer, ProductListSerializer, \
    CategoryListSerializer, ProductDetailSerializer, ProductCreateSerializer, ProductUpdateSerializer
from .filters import ProductFilter


# class UserCreateAPIView(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserCreateSerializer
#
#
# class UserListAPIView(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserListSerializer


class UserCreateListAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    # pagination_class = PageNumberPagination
    # page_size = 2
    # filter_backends = DjangoFilterBackend,
    # filterset_fields = ('first_name', 'last_name', 'username')
    filterset_class = ProductFilter

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        elif self.request.method == 'GET':
            return UserCreateSerializer
        return super().get_serializer_class()


class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    # filterset_fields = ('name', 'category', 'owner')
    # filterset_class = ProductFilter
    # filter_backends = DjangoFilterBackend, SearchFilter
    # search_fields = 'name', 'description'
    # permission_classes = [IsAuthenticated, ]


# class ProductListAPIView(APIView):
#
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductListSerializer(products, many=True).data
#         # print(serializer)
#         # if serializer.is_valid():
#         data = {
#             'products': f'All products {len(products)}',
#             'status': status.HTTP_200_OK,
#             'data': serializer
#         }
#         return Response(data)


class ProductDetailAPIView(APIView):
    def get(self, request, pk):
        # try:
        #     product = Product.objects.get(id=pk)
        #     serializer = ProductDetailSerializer(product).data
        #     data = {
        #         'status': status.HTTP_200_OK,
        #         'data': serializer
        #     }
        #     return Response(data)
        # except:
        #     return Response(status=status.HTTP_404_NOT_FOUND)

        # product = Product.objects.get(id=pk)
        product = get_object_or_404(Product.objects.all(), id=pk)
        serializer = ProductDetailSerializer(product).data
        data = {
            'status': status.HTTP_200_OK,
            'data': serializer
        }
        return Response(data)


class ProductCreateAPIView(APIView):
    def post(self, request):
        product = request.data
        serializer = ProductCreateSerializer(data=product)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        # print(product)


class ProductUpdateAPIView(APIView):
    def put(self, request, pk):
        product = Product.objects.get(id=pk)
        data = request.data
        serializer = ProductUpdateSerializer(data=data, instance=product, partial=True)
        if serializer.is_valid():
            serializer.save()
            a = {
                'status': status.HTTP_200_OK,
                'data': serializer.data
            }
            return Response(a)
        # print(data)




class ProductDestroyAPIView(APIView):
    def delete(self, request, pk):
        # product = get_object_or_404(Product, id=pk)
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


