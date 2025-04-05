from django.shortcuts import render


def index(request):
    return render(request, 'e_commerce/index.html')

def about(request):
    return render(request, 'e_commerce/about-us.html')

def cart(request):
    return render(request, 'e_commerce/cart.html')

def checkout(request):
    return render(request, 'e_commerce/checkout.html')

def contact(request):
    return render(request, 'e_commerce/contact-us.html')

def single_post(request):
    return render(request, 'e_commerce/single-post.html')

def wishlist(request):
    return render(request, 'e_commerce/wishlist.html')

def shop_cart(request):
    return render(request, 'e_commerce/shop-cart.html')

def shop_grid(request):
    return render(request, 'e_commerce/shop-grid.html')

def book_list(request):
    return render(request, 'e_commerce/books-list.html')

def book_detail(request):
    return render(request, 'e_commerce/books-detail.html')

def book_grid_view(request):
    return render(request, 'e_commerce/books-grid-view.html')

def book_grid_left_sidebar(request):
    return render(request, 'e_commerce/books-grid-left-sidebar.html')

def book_grid_no_sidebar(request):
    return render(request, 'e_commerce/books-grid-no-sidebar.html')

def book_list_view_sidebar(request):
    return render(request, 'e_commerce/books-list-view-sidebar.html')

def book_grid_view_sidebar(request):
    return render(request, 'e_commerce/books-grid-view-sidebar.html')

def blog_detail(request):
    return render(request, 'e_commerce/blog-detail.html')

def blog_grid_left_sidebar(request):
    return render(request, 'e_commerce/blog-grid-left-sidebar.html')

def blog_grid_no_sidebar(request):
    return render(request, 'e_commerce/blog-grid-no-sidebar.html')

def shop_checkout(request):
    return render(request, 'e_commerce/shop-checkout.html')

def my_profile(request):
    return render(request, 'e_commerce/my_profile.html')

def shop_login(request):
    return render(request, 'e_commerce/shop_login.html')

def shop_registration(request):
    return render(request, 'e_commerce/shop-registration.html')

def services(request):
    return render(request, 'e_commerce/services.html')