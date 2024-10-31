from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from cinetic.settings import AUTH_USER_MODEL


class Customer(AbstractUser):
    user_email = models.EmailField(max_length=60, unique=True, blank=False)
    USERNAME_FIELD = "user_email"
    EMAIL_FIELD = "user_email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username", "password"]


################################################################################################################

class Category(models.Model):
    name = models.CharField(max_length=80, blank=False, verbose_name="Nom de la catégorie")
    description = models.CharField(max_length=80, blank=True, verbose_name="Description")
    created_at = models.DateTimeField(blank=True, null=True, verbose_name="Date de création")

    def __str__(self):
        return f"{self.name}"


class Discount(models.Model):
    name = models.CharField(max_length=80, blank=False, verbose_name="Libellé de la promotion")
    description = models.CharField(max_length=255, blank=False, verbose_name="Description")
    percentage = models.SmallIntegerField(verbose_name="Pourcentage par rapport au prix")
    created_at = models.DateTimeField(blank=True, null=True, verbose_name="Date de création")

    def __str__(self):
        return f"{self.name}"


class Size(models.Model):
    size_key = models.CharField(blank=True, verbose_name="Taille")
    display = models.CharField(blank=True, verbose_name="Valeur de taille")

    def __str__(self):
        return f"{self.size_key}"


class Color(models.Model):
    color_key = models.CharField(blank=True, verbose_name="Couleur")
    display = models.CharField(blank=True, verbose_name="Valeur de couleur")

    def __str__(self):
        return f"{self.color_key}"


class Image(models.Model):
    path_1 = models.ImageField(upload_to="madishop", blank=True, null=True, max_length=100, verbose_name="Img1")

    def __str__(self):
        return f"{self.path_1}"


class Article(models.Model):
    name = models.TextField(verbose_name="Nom du produit")
    desc_short = models.CharField(max_length=255, blank=False, verbose_name="Desc courte")
    desc_full = models.TextField(verbose_name="Desc longue")
    weight = models.SmallIntegerField(blank=True, null=True, verbose_name="Poids")
    capacity = models.SmallIntegerField(blank=True, null=True, verbose_name="Contenance")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Catégorie")
    images = models.ManyToManyField(Image)
    created_at = models.DateTimeField(blank=True, null=True, verbose_name="Date de création")

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("madishop:prd_detail", kwargs={"category": self.category, "product_id": self.pk})

    def get_image(self):
        return ",".join([str(p.path_1) for p in self.images.all()])


class Product(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Catégorie")
    sku = models.CharField(unique=True, max_length=5, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Prix")
    discount = models.ForeignKey(Discount, on_delete=models.DO_NOTHING, verbose_name="Remises")
    sizes = models.ManyToManyField(Size)
    colors = models.ManyToManyField(Color)
    images = models.ManyToManyField(Image)
    in_stock = models.SmallIntegerField(default=10, verbose_name="Quantité en stock")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.article}"

    def get_size(self):
        return ",".join([s.size_key for s in self.sizes.all()])

    def get_color(self):
        return ",".join([c.color_key for c in self.colors.all()])

    def get_image(self):
        return ",".join([str(p.path_1) for p in self.images.all()])

    def get_absolute_url(self):
        return reverse("madishop:prd_detail",
                       kwargs={"category": self.article.category.name, "article_id": self.article.pk})

################################################################################################################

class CartItem(models.Model):
    """ Temporary table for cart item """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Produit dans le panier")
    quantity = models.SmallIntegerField(default=0, verbose_name="Quantité commandée")
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0, verbose_name="Total")

    def __str__(self):
        return f"{self.product}"

    def add_or_modifQty_item(self, prd, nb_quantity, action):
        if str(action) == "add":
            self.quantity += nb_quantity
        elif str(action) == "modify":
            self.quantity = nb_quantity
        self.total = prd.price * self.quantity
        self.save()
        return self.total

    def Taille(self):
        return f"{self.product.get_size()}"

    def Couleur(self):
        return f"{self.product.get_color()}"


class Order(models.Model):
    """ Table for validated order """

    pass
    # customer = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Nom du client") à remettre + tard
    # cart = models.ManyToManyField(CartItem)# A vérifier, CartItem est associé à 1 seul customer !!!
    # cart = models.ForeignKey(CartItem, on_delete=models.CASCADE, verbose_name="Article acheté")
    # created_at = models.DateTimeField(blank=True, null=True, verbose_name="Date de création")
    # modified_at = models.DateTimeField(blank=True, null=True, verbose_name="Date de modification")

    # def __str__(self):
    #     return f"{self.cart}"


# class Payment(models.Model):
    # """ Table for payment mode """

    # order = models.ForeignKey(Order, on_delete=models.DO_NOTHING) # A vérifier !!!
    # amount = models.DecimalField()
    # provider = models.CharField(max_length=20)
    # status = models.CharField(max_length=15) # A Vérifier !!!
    # created_at = models.DateTimeField()

