from django.db import models


class Categorie(models.Model):

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

    nom = models.CharField(verbose_name="Nom", max_length=100, unique=True)

    # Standards
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom


class Tag(models.Model):

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    nom = models.CharField(verbose_name="Nom", max_length=100, unique=True)

    # Standards
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom


class Livre(models.Model):
    FORMAT_CHOICES = [
        ('Paperback', 'Paperback'),
        ('Hardcover', 'Hardcover'),
        ('Ebook', 'Ebook'),
        ('Audiobook', 'Audiobook'),
    ]

    LANGUE_CHOICES = [
        ('FR', 'Français'),
        ('EN', 'English'),
        ('ES', 'Español'),
        ('DE', 'Deutsch'),
        # tu peux en ajouter d'autres
    ]

    titre = models.CharField(max_length=255)
    couverture = models.ImageField(upload_to='couvertures/')
    auteur = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, unique=True)
    langue = models.CharField(max_length=2, choices=LANGUE_CHOICES)
    format = models.CharField(max_length=20, choices=FORMAT_CHOICES)
    date_publication = models.DateField()
    editeur = models.CharField(max_length=255)
    nombre_pages = models.PositiveIntegerField()
    nombre_chapitres = models.PositiveIntegerField()
    nombre_topics = models.PositiveIntegerField()

    categorie_ids = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, related_name='livres')
    tags_ids = models.ManyToManyField(Tag, blank=True)

    description = models.TextField(blank=True)  # pour un résumé ou une description

    def __str__(self):
        return self.titre