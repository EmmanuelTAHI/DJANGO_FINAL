from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from .form import AuthForm
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


def index(request):
    return render(request, 'e_commerce/index.html')

def about(request):
    return render(request, 'e_commerce/about-us.html')

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
    return render(request, 'e_commerce/my-profile.html')

def services(request):
    return render(request, 'e_commerce/services.html')

# ==============================
# 🔐 Authentification (Connexion, Inscription, Déconnexion)
# ==============================

def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')  # Vérifie si "Se souvenir de moi" est coché

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            if remember_me:
                # Prolonge la session à 30 jours (comme Amazon)
                request.session.set_expiry(30 * 24 * 60 * 60)  # 30 jours en secondes
            else:
                # La session expire à la fermeture du navigateur
                request.session.set_expiry(0)

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
            user.is_active = False  # Désactiver le compte jusqu'à activation
            user.is_superuser = True  # On donne les droits admin
            user.is_staff = True
            user.save()

            # Génération du lien d'activation
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            domain = get_current_site(request).domain
            activation_link = f"http://{domain}/activate/{uid}/{token}/"

            # Contenu du mail
            subject = "Activation de votre compte"
            message = f"""
            Bonjour {user.username},

            Merci de vous être inscrit. Veuillez cliquer sur le lien ci-dessous pour activer votre compte :

            {activation_link}

            Si vous n'avez pas demandé cette inscription, ignorez cet email.

            Merci,
            L'équipe de support.
            """

            # Envoi du mail
            email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [user.email])
            email.send(fail_silently=False)
            return redirect('login')  # Redirige l'utilisateur

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
        login(request, user)  # Connexion automatique après activation
        return redirect("index")

    return render(request, "registration/activation_failed.html")  # Page d’erreur