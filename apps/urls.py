from django.contrib import admin
from django.urls import path
from apps.views import UserDetailAPIView, UserUpdateAPIView, UserDestroyAPIView, \
    UserCreateListAPIView, UserRetrieveUpdateDestroyAPIView, ProductListAPIView, CategoryListAPIView, \
    ProductDetailAPIView, ProductCreateAPIView, ProductDestroyAPIView, ProductUpdateAPIView

urlpatterns = [
    #1
    # path('user-create/', UserCreateAPIView.as_view(), name='user_create'),
    # path('user-list/', UserListAPIView.as_view(), name='user_list'),

    #2
    # path('users/', UserCreateListAPIView.as_view(), name='user_list'),


    #1
    # path('user/<int:pk>/', UserDetailAPIView.as_view(), name='user_detail'),
    # path('user-update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('user-delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),

    #2
    # path('user/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user_delete'),


    path('products/', ProductListAPIView.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product'),
    path('product-delete/<int:pk>/', ProductDestroyAPIView.as_view(), name='product_delete'),
    path('product-update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_update'),
    path('product-create/', ProductCreateAPIView.as_view(), name='create-product'),
    path('category', CategoryListAPIView.as_view(), name='category'),
]
