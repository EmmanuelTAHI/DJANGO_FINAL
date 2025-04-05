from django.shortcuts import render


def index(request):
    livres = (Livre.objects.all())  # Récupère tous les livres
    return render(request, 'e_commerce/index.html', {'livres': livres})

def about(request):
    return render(request, 'e_commerce/about.html')

def shop(request):
    return render(request, 'e_commerce/shop.html')

def blog(request):
    return render(request, 'e_commerce/blog.html')

def cart(request):
    return render(request, 'e_commerce/cart.html')

def checkout(request):
    return render(request, 'e_commerce/checkout.html')

def contact(request):
    return render(request, 'e_commerce/contact.html')


def single_post(request):
    return render(request, 'e_commerce/single-post.html')

# Vue pour afficher les détails d'un livre
def single_product(request, livre_id):
    livre = get_object_or_404(Livre, id=livre_id)
    return render(request, 'e_commerce/single-product.html', {'livre': livre})