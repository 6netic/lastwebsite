from django.contrib import admin
from . models import Category, Discount, Size, Color, Image, Article, Product
from . models import Customer, CartItem, Order
# from django.contrib.auth.admin import UserAdmin
from . models import Customer


class UserAdmin(admin.ModelAdmin):
    fields = ["user_email", "username", "first_name", "last_name"]
    list_display = ["username", "user_email"]


class CategoryAdmin(admin.ModelAdmin):
    fields = ["name", "description", "created_at", "modified_at", "deleted_at"]
    readonly_fields = ["created_at"]
    list_display = ["name", "description"]


class DiscountAdmin(admin.ModelAdmin):
    fields = ["name", "description", "percentage", "created_at"]
    readonly_fields = ["created_at"]
    list_display = ["name", "description", "percentage"]


class SizeAdmin(admin.ModelAdmin):
    fields = ["size_key", "display"]
    list_display = ["size_key", "display"]


class ColorAdmin(admin.ModelAdmin):
    fields = ["color_key", "display"]
    list_display = ["color_key", "display"]


class ImageAdmin(admin.ModelAdmin):
    fields = ["path_1"]
    list_display = ["path_1"]


class ArticleAdmin(admin.ModelAdmin):
    fields = ["name", "category", "desc_short", "desc_full", "weight", "capacity", "images", "created_at"]
    readonly_fields = ["created_at"]
    list_display = ("name", "category", "get_image")
    list_filter = ["name"]
    search_fields = ["name"]

# class ProductGalleryInLine(admin.StackedInline):
#     model = ProductGallery
#     extra = 0
#     max_num = 0

# article(fk) - sku - price - discount(fk) - sizes(m2m) - colors(m2m) - images(m2m) - in_stock(int) - is_active
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        # ("Catégorie du produit", {"fields": ["category"]}),
        ("Informations sur le produit", {
            "fields": [
                "sku", "article", "sizes", "colors", "images", "discount", "price", "in_stock", "is_active"
            ]
        }),
        # ("Dates enregistrées", {
        #     "fields": ["created_at", "modified_at", "deleted_at"]
        # }),
        # Faire apparaitre l'inventaire du produit ici
    ]
    list_display = ("article", "get_size", "get_color", "get_image", "discount", "price", "in_stock")
    list_filter = ["article"]
    search_fields = ["article"]
    # inlines = [ProductGalleryInLine]
    # readonly_fields = ("sizes", "colors", "images")


class CartItemAdmin(admin.ModelAdmin):
    fields = ["product", "quantity", "total"]
    list_display = ["product", "Taille", "Couleur", "quantity", "total"]



admin.site.register(Category, CategoryAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Customer, UserAdmin)

# admin.site.register(Order)