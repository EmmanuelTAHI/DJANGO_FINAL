from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('book_list/', views.book_list, name='book_list'),
    path('book_detail/', views.book_detail, name='book_detail'),
    path('book_grid_view/', views.book_grid_view, name='book_grid_view'),
    path('book_grid_left_sidebar/', views.book_grid_left_sidebar, name='book_grid_left_sidebar'),
    path('book_grid_no_sidebar/', views.book_grid_no_sidebar, name='book_grid_no_sidebar'),
    path('book_list_view_sidebar/', views.book_list_view_sidebar, name='book_list_view_sidebar'),
    path('book_grid_view_sidebar/', views.book_grid_view_sidebar, name='book_grid_view_sidebar'),
    path('blog_detail/', views.blog_detail, name='blog_detail'),
    path('blog_grid_left_sidebar/', views.blog_grid_left_sidebar, name='blog_grid_left_sidebar'),
    path('blog_grid_no_sidebar/', views.blog_grid_no_sidebar, name='blog_grid_no_sidebar'),
    path('shop_cart/', views.shop_cart, name='shop_cart'),
    path('shop_login/', views.shop_login, name='shop_login'),
    path('shop_registration/', views.shop_registration, name='shop_registration'),
    path('shop_grid/', views.shop_grid, name='shop_grid'),
    path('shop_checkout/', views.shop_checkout, name='shop_checkout'),
    path('my_profile/', views.my_profile, name='my_profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Gestion des fichiers médias en mode debug
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
