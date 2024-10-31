from django.core.management.base import BaseCommand
from madishop.models import Category, Discount, Size, Color, Image, Product, Article
from django.utils import timezone


class Command(BaseCommand):
    help = "Populates 'Madishop Product' tables."

    def handle(self, *args, **options):
        # Populates 'Article' table #################################################################################
        items = [
            # name - desc_short - desc_full - weight - capacity - category - images - created_at
            [
                "Liqueur St-Germain",
                "Polyvalente et élégante, la liqueur St-Germain est devenue un indispensable chez les barmans "
                "les plus réputés !",
                "La liqueur St-Germain a été créée en 2007 par Rob Cooper, distillateur de troisième génération, "
                "épaulé par certains des meilleurs mixologues et producteurs de liqueurs françaises traditionnelles. "
                "Elle rend hommage à l’esprit du Paris des années 1920. Pas moins de 1000 fleurs de sureau fraîches "
                "sont nécessaires à la réalisation d’une seule bouteille. Produite en quantité limitée, chaque bouteille"
                " de St-Germain est numérotée et millésimée, l'année ainsi indiquée sur l’étiquette est celle de la "
                "mise en bouteille. Ses accents de fruits exotiques et de subtiles notes florales créent un goût "
                "sublime inégalé !",
                0,
                700,
                "Alcools",
                "madishop/alcool/liqueur-st-germain.jpg"
            ],
            [
                "Liqueur - Italicus",
                "Italicus, LE NOUVEAU spiritueux italien au succès mondial !",
                "L'une des boissons les plus populaires en Italie depuis le 19ème siècle. Italicus est un spiritueux "
                "issu d'une petite distillerie familiale de Moncalieri, près de Turin. Sa recette est restée inchangée "
                "et est devenue un incontournable des apéritifs partout dans le Monde ces dernières années. "
                "Composée d'une infusion de bergamote, cédrat, camomille et gentiane, cette liqueur est délicate et "
                "apporte une subtile amertume à la dégustation la rendant équilibrée et fraîche, aux saveurs "
                "d'agrumes et de rose. Associé la à du Prosecco et des glaçons, et découvrez l'Italicus dans "
                "toute sa splendeur !",
                0,
                700,
                "Alcools",
                "madishop/alcool/liqueur-italicus.jpg"
            ],
            # name - desc_short - desc_full - weight - capacity - category - images - created_at
            [
                "ICE COOL - Fraise Framboise Basilic",
                "E-liquide Fraise Framboise Basilic de la gamme Ice Cool.",
                "Ratio PG/VG : 50/50. Fabrication Française.",
                0,
                50,
                "E-liquides",
                "madishop/eliquid/ic-fraise-framboise-basilic-50.jpg",
            ],
            [
                "ICE COOL - Framboise Bleue Pitaya",
                "E-liquide Framboise Bleue Pitaya de la gamme Ice Cool.",
                "Ratio PG/VG : 50/50. Fabrication Française.",
                0,
                50,
                "E-liquides",
                "madishop/eliquid/ic-framboise-bleue-pitaya.jpg",
            ],
            # name - desc_short - desc_full - weight - capacity - category - images - created_at
            [
                "T-shirt ras de cou, broderie fougère - La Redoute Collections",
                "",
                "<b>Détails produit</b><br>&nbsp;•&nbsp;&nbsp;Manches courtes<br>&nbsp;•&nbsp;&nbsp;"
                "Col rond<br>&nbsp;•&nbsp;&nbsp;Motif&nbsp;brodé fougère<br><b>Mesures du produit en taille 40/M&nbsp;"
                "</b><br>&nbsp;•&nbsp;&nbsp;Longueur des manches : 23,5 cm&nbsp;<br><br><b>Composition et Entretien</b>"
                "<br>&nbsp;•&nbsp;&nbsp;100% coton<br>&nbsp;•&nbsp;&nbsp;Pour l'entretien, merci de vous référer aux "
                "indications figurant sur l'étiquette du produit<br>",
                0,
                0,
                "Tee-shirts",
                "madishop/tshirt/tshirt_laredoute_collections_green.jpg",
            ],
            [
                "T-shirt imprimé montagne - JACK & JONES",
                "",
                "<b>Détails produit</b><br>&nbsp;•&nbsp;&nbsp;Manches courtes<br>&nbsp;•&nbsp;&nbsp;Col "
                "rond<br>&nbsp;•&nbsp;&nbsp;Motif&nbsp;imprimé<br><br><b>Composition et Entretien</b><br>"
                "&nbsp;•&nbsp;&nbsp;100% coton<br>&nbsp;•&nbsp;&nbsp;Pour l'entretien, merci de vous référer aux "
                "indications figurant sur l'étiquette du produit<br>",
                0,
                0,
                "Tee-shirts",
                "madishop/tshirt/tshirt_jjones_mont_white.jpg",
            ],

        ]
        try:
            for item in items:
                img = Image.objects.get(path_1=item[6])
                entry = Article.objects.create(
                    name=item[0],
                    desc_short=item[1],
                    desc_full=item[2],
                    weight=item[3],
                    capacity=item[4],
                    category=Category.objects.get(name=item[5]),
                    created_at=timezone.now()
                )
                entry.images.add(img)
            print("Les données ont bien été chargées dans la table 'Article'.")
        except KeyError:
            print("Une erreur s'est produite. Ces données sont déjà présentes dans la table 'Article'.")
        # name - desc_short - desc_full - weight - capacity - category - images - created_at

"""        
        # Populates 'Product' table #################################################################################
        items = [
            
            
            
            
            

        ]
        try:
            for item in items:
                Product.objects.create(
                    category=ProductCategory.objects.get(name=item[0]),
                    discount=ProductDiscount.objects.get(name=item[1]),
                    sku=item[2],
                    name=item[3],
                    desc_short=item[4],
                    desc_full=item[5],
                    size=ProductSize.objects.get(name=item[6]),
                    color=ProductColor.objects.get(name=item[7]),
                    weight=item[8],
                    capacity=item[9],
                    price=item[10],
                    image_path=item[11],
                    created_at=timezone.now()
                )
            print("Les données ont bien été chargées dans la table 'Product'.")
        except KeyError:
            print("Une erreur s'est produite. Ces données sont déjà présentes dans la table 'Product'.")

"""