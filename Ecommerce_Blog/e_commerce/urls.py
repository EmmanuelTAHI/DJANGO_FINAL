from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import activate_account, book_detail

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('toggle-wishlist/', views.toggle_wishlist, name='toggle_wishlist'),
    path('remove-from-wishlist/<int:livre_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('remove-from-cart/<int:livre_id>/', views.remove_from_cart, name='remove-from-cart'),
    path('book-list/', views.book_list, name='book-list'),
    path('book-detail/<int:livre_id>/', book_detail, name="book-detail"),
    path('book-grid-view/', views.book_grid_view, name='book-grid-view'),
    path('book-grid-left-sidebar/', views.book_grid_left_sidebar, name='book-grid-left-sidebar'),
    path('book-grid-no-sidebar/', views.book_grid_no_sidebar, name='book-grid-no-sidebar'),
    path('book-list-view-sidebar/', views.book_list_view_sidebar, name='book-list-view-sidebar'),
    path('book-grid-view-sidebar/', views.book_grid_view_sidebar, name='book-grid-view-sidebar'),
    path('blog-detail/', views.blog_detail, name='blog-detail'),
    path('blog-grid-left-sidebar/', views.blog_grid_left_sidebar, name='blog-grid-left-sidebar'),
    path('blog-grid-no-sidebar/', views.blog_grid_no_sidebar, name='blog-grid-no-sidebar'),
    path('login/', views.connexion, name='login'),
    path('register/', views.inscription, name='register'),
    path("deconnexion/", views.deconnexion, name="deconnexion"),
    path('activate/<uidb64>/<token>/', activate_account, name='activate-account'),
    path('add-to-cart/<int:livre_id>/', views.add_to_cart, name='add-to-cart'),
    path('shop-grid/', views.shop_grid, name='shop-grid'),
    path('shop-cart/', views.shop_cart, name='shop-cart'),
    path('shop-cart/<int:livre_id>/', views.add_to_cart, name='shop-cart'),  # Ajoute ceci
    path('shop-checkout/', views.shop_checkout, name='shop-checkout'),
    path('my-profile/', views.my_profile, name='my-profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Gestion des fichiers médias en mode debug
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
