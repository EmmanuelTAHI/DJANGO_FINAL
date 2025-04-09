from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .form import AuthForm
from .models import Livre, Wishlist
from django.http import JsonResponse


# ==============================
# 🌐 Pages générales
# ==============================

def index(request):
    livres = (Livre.objects.all())  # Récupère tous les livres
    return render(request, 'e_commerce/index.html', {'livres': livres})

def about(request):
    return render(request, 'e_commerce/about-us.html')

def contact(request):
    return render(request, 'e_commerce/contact-us.html')

def services(request):
    return render(request, 'e_commerce/services.html')

def my_profile(request):
    return render(request, 'e_commerce/my-profile.html')

# ==============================
# 🛒 Pages E-commerce / Boutique
# ==============================


def checkout(request):
    return render(request, 'e_commerce/checkout.html')

@login_required
def add_to_cart(request, livre_id):
    try:
        livre = Livre.objects.get(id=livre_id)
        # Logique pour ajouter au panier (par exemple, avec un modèle Cart)
        # Pour l'instant, redirige vers la page du panier
        return redirect('shop_cart')  # Redirige vers la page du panier
    except Livre.DoesNotExist:
        return redirect('wishlist')  # Retourne à la wishlist si le livre n'existe pas

def wishlist(request):
    if request.user.is_authenticated:
        wishlist_items = Wishlist.objects.filter(user=request.user)
        context = {'wishlist_items': wishlist_items}
        return render(request, 'e_commerce/wishlist.html', context)
    else:
        # Si l'utilisateur n'est pas connecté, redirige ou affiche un message
        return render(request, 'e_commerce/wishlist.html', {'wishlist_items': []})

@login_required
def toggle_wishlist(request):
    if request.method == 'POST':
        livre_id = request.POST.get('livre_id')
        try:
            livre = Livre.objects.get(id=livre_id)
            wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, livre=livre)
            if not created:
                wishlist_item.delete()
                return JsonResponse({'status': 'removed'})
            return JsonResponse({'status': 'added'})
        except Livre.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Livre non trouvé'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Requête invalide'}, status=400)

@login_required
def remove_from_wishlist(request, livre_id):
    try:
        wishlist_item = Wishlist.objects.get(user=request.user, livre=Livre.objects.get(id=livre_id))
        wishlist_item.delete()
    except Wishlist.DoesNotExist:
        pass
    return redirect('wishlist')

def shop_cart(request):
    return render(request, 'e_commerce/shop-cart.html')

def shop_checkout(request):
    return render(request, 'e_commerce/shop-checkout.html')

def shop_grid(request):
    return render(request, 'e_commerce/shop-grid.html')

# ==============================
# 📚 Pages Livres
# ==============================

def book_list(request):
    livres = Livre.objects.all()
    return render(request, 'e_commerce/books-list.html', {'livres': livres})

def book_detail(request, livre_id):
    livre = get_object_or_404(Livre, id=livre_id)
    return render(request, 'e_commerce/books-detail.html', {'livre': livre})

def book_grid_view(request):
    livres = Livre.objects.all()  # Utilise le nom de ton modèle (Book ou autre)
    return render(request, 'e_commerce/books-grid-view.html', {'livres': livres})

def book_grid_left_sidebar(request):
    return render(request, 'e_commerce/books-grid-left-sidebar.html')

def book_grid_no_sidebar(request):
    return render(request, 'e_commerce/books-grid-no-sidebar.html')

def book_list_view_sidebar(request):
    return render(request, 'e_commerce/books-list-view-sidebar.html')

def book_grid_view_sidebar(request):
    livres = Livre.objects.all()
    wishlist_ids = []
    if request.user.is_authenticated:
        wishlist_ids = Wishlist.objects.filter(user=request.user).values_list('livre_id', flat=True)
    return render(request, 'e_commerce/books-grid-view-sidebar.html', {'livres': livres,'wishlist_ids': wishlist_ids})

# ==============================
# 📝 Pages Blog
# ==============================

def blog_detail(request):
    return render(request, 'e_commerce/blog-detail.html')

def blog_grid_left_sidebar(request):
    return render(request, 'e_commerce/blog-grid-left-sidebar.html')

def blog_grid_no_sidebar(request):
    return render(request, 'e_commerce/blog-grid-no-sidebar.html')

def single_post(request):
    return render(request, 'e_commerce/single-post.html')

# ==============================
# 🔐 Authentification (Connexion / Inscription / Activation)
# ==============================

def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if remember_me:
                request.session.set_expiry(30 * 24 * 60 * 60)  # 30 jours
            else:
                request.session.set_expiry(0)  # Session expire à la fermeture
            return redirect('index')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    return render(request, 'registration/shop-login.html')

def deconnexion(request):
    logout(request)
    return redirect('index')

def inscription(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.is_superuser = True
            user.is_staff = True
            user.save()

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            domain = get_current_site(request).domain
            activation_link = f"http://{domain}/activate/{uid}/{token}/"

            subject = "Activation de votre compte"
            message = f"""
            Bonjour {user.username},

            Merci de vous être inscrit. Veuillez cliquer sur le lien ci-dessous pour activer votre compte :

            {activation_link}

            Si vous n'avez pas demandé cette inscription, ignorez cet email.

            Merci,
            L'équipe de support.
            """
            email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [user.email])
            email.send(fail_silently=False)
            return redirect('login')
    else:
        form = AuthForm()
    return render(request, 'registration/shop-registration.html', {'form': form})

def activate_account(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        messages.error(request, "Le lien d'activation est invalide ou a expiré.")

    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect("index")

    return render(request, "registration/activation_failed.html")