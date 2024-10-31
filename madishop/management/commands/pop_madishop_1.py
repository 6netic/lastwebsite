from django.core.management.base import BaseCommand
from madishop.models import Category, Discount, Size, Color
from django.utils import timezone


class Command(BaseCommand):
    help = "Populates 'Madishop' ProductCategory, ProductDiscount, ProductSize and ProductColor tables."

    def handle(self, *args, **options):
        # Populates 'Category' table #################################################################################
        categories = [
            ["Alcools", "Catégorie des Alcools en vente sur ce site."],
            ["E-liquides", "Catégorie des E-liquides pour les vapoteuses."],
            ["Tee-shirts", "Catégorie des Tee-shirts en vente sur ce site."]
        ]
        try:
            for item in categories:
                Category.objects.create(
                    name=item[0],
                    description=item[1],
                    created_at=timezone.now()
                )
            print("Les données ont bien été chargées dans la table 'Category'.")
        except KeyError:
            print("Une erreur s'est produite. Ces données sont déjà présentes dans la table 'Category'.")

        # Populates 'Discount' table ##########################################################################
        discounts = [
            ["Aucune remise", "Prix normal du produit donc 100% du prix de l'article.", 100],
            ["Promotion de Noël", "Une remise de 30% est appliquée pour la période des fêtes de Noel.", 70],
            ["Promotion du Black Friday", "Une remise de 45% est appliquée pour le Black Friday.", 55]
        ]
        try:
            for item in discounts:
                Discount.objects.create(
                    name=item[0],
                    description=item[1],
                    percentage=item[2],
                    created_at=timezone.now()
                )
            print("Les données ont bien été chargées dans la table 'Discount'.")
        except KeyError:
            print("Une erreur s'est produite. Ces données sont déjà présentes dans la table 'ProductDiscount'.")

        # Populates 'Size' table ###############################################################################
        sizes = [
            ["", ""], ["s", "Taille S"], ["m", "Taille M"],
            ["l", "Taille L"], ["xl", "Taille XL"], ["xxl", "Taille XXL"]
        ]
        try:
            for item in sizes:
                Size.objects.create(size_key=item[0], display=item[1])
            print("Les données ont bien été insérées dans la table 'Size'.")
        except KeyError:
            print("Une erreur s'est produite. Ces données sont déjà présentes dans la table 'ProductSize'.")

        # Populates 'Color' table ##############################################################################
        colors = [
            ["", ""], ["green", "Vert"], ["light_green", "Vert clair"], ["dark_green", "Vert foncé"],
            ["blue", "Bleu"], ["light_blue", "Bleu clair"], ["dark_blue", "Bleu foncé"], ["black", "Noir"],
            ["white", "Blanc"], ["beige", "Beige"], ["grey", "Gris"], ["cream", "Crème"], ["pink", "Rose"],
            ["red", "Rouge"], ["yellow", "Jaune"], ["orange", "Orange"], ["lilas", "Lilas"], ["kaki", "Kaki"],
            ["dark_indigo", "Indigo foncé"], ["marron", "Marron"], ["maroon", "Bordeaux"], ["menthol", "Menthol"]
        ]
        try:
            for item in colors:
                Color.objects.create(color_key=item[0], display=item[1])
            print("Les données ont bien été insérées dans la table 'Color'.")
        except KeyError:
            print("Une erreur s'est produite. Ces données sont déjà présentes dans la table 'Color'.")