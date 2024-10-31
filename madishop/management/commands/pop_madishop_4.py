from django.core.management.base import BaseCommand
from madishop.models import Category, Discount, Size, Color, Image, Product, Article
from django.utils import timezone


class Command(BaseCommand):
    help = "Populates 'Madishop Product' tables."

    def handle(self, *args, **options):
        # Populates 'Article' table #################################################################################
        items = [
            # article(fk) - sku - price - discount(fk) - sizes(m2m) - colors(m2m) - images(m2m)
            [
                "Liqueur St-Germain",
                "AB001",
                39.90,
                "Aucune remise",
                "",
                "",
                "madishop/alcool/liqueur-st-germain.jpg"
            ],
            [
                "Liqueur - Italicus",
                "AB002",
                32.90,
                "Aucune remise",
                "",
                "",
                "madishop/alcool/liqueur-italicus.jpg"
            ],
            # article(fk) - sku - price - discount(fk) - sizes(m2m) - colors(m2m) - images(m2m)
            [
                "ICE COOL - Fraise Framboise Basilic",
                "AB021",
                19.90,
                "Aucune remise",
                "",
                "",
                "madishop/eliquid/ic-fraise-framboise-basilic-50.jpg",
            ],
            [
                "ICE COOL - Framboise Bleue Pitaya",
                "AB022",
                19.90,
                "Aucune remise",
                "",
                "",
                "madishop/eliquid/ic-framboise-bleue-pitaya.jpg",
            ],
            # article(fk) - sku - price - discount(fk) - sizes(m2m) - colors(m2m) - images(m2m)
            [
                "T-shirt ras de cou, broderie fougère - La Redoute Collections",
                "AB048",
                12.70,
                "Aucune remise",
                "s",
                "green",
                "madishop/tshirt/tshirt_laredoute_collections_green.jpg",
            ],
            [
                "T-shirt ras de cou, broderie fougère - La Redoute Collections",
                "AB049",
                12.70,
                "Aucune remise",
                "m",
                "green",
                "madishop/tshirt/tshirt_laredoute_collections_green.jpg",
            ],
            [
                "T-shirt ras de cou, broderie fougère - La Redoute Collections",
                "AB050",
                12.70,
                "Aucune remise",
                "l",
                "green",
                "madishop/tshirt/tshirt_laredoute_collections_green.jpg",
            ],
            [
                "T-shirt ras de cou, broderie fougère - La Redoute Collections",
                "AB051",
                12.70,
                "Aucune remise",
                "xl",
                "green",
                "madishop/tshirt/tshirt_laredoute_collections_green.jpg",
            ],




            [
                "T-shirt imprimé montagne - JACK & JONES",
                "AB052",
                26.30,
                "Aucune remise",
                "s",
                "white",
                "madishop/tshirt/tshirt_jjones_mont_white.jpg",
            ],
            [
                "T-shirt imprimé montagne - JACK & JONES",
                "AB053",
                26.30,
                "Aucune remise",
                "m",
                "white",
                "madishop/tshirt/tshirt_jjones_mont_white.jpg",
            ],
            [
                "T-shirt imprimé montagne - JACK & JONES",
                "AB054",
                26.30,
                "Aucune remise",
                "l",
                "white",
                "madishop/tshirt/tshirt_jjones_mont_white.jpg",
            ],
            [
                "T-shirt imprimé montagne - JACK & JONES",
                "AB055",
                26.30,
                "Aucune remise",
                "xl",
                "white",
                "madishop/tshirt/tshirt_jjones_mont_white.jpg",
            ],
            [
                "T-shirt imprimé montagne - JACK & JONES",
                "AB056",
                27.20,
                "Aucune remise",
                "s",
                "green",
                "madishop/tshirt/tshirt_jjones_mont_green.jpg",
            ],
            [
                "T-shirt imprimé montagne - JACK & JONES",
                "AB057",
                27.20,
                "Aucune remise",
                "m",
                "green",
                "madishop/tshirt/tshirt_jjones_mont_green.jpg",
            ],
            [
                "T-shirt imprimé montagne - JACK & JONES",
                "AB058",
                27.20,
                "Aucune remise",
                "l",
                "green",
                "madishop/tshirt/tshirt_jjones_mont_green.jpg",
            ],
            [
                "T-shirt imprimé montagne - JACK & JONES",
                "AB059",
                27.20,
                "Aucune remise",
                "xl",
                "green",
                "madishop/tshirt/tshirt_jjones_mont_green.jpg",
            ],
            [
                "T-shirt imprimé montagne - JACK & JONES",
                "AB060",
                27.20,
                "Aucune remise",
                "s",
                "grey",
                "madishop/tshirt/tshirt_jjones_mont_grey.jpg",
            ],
            [
                "T-shirt imprimé montagne - JACK & JONES",
                "AB061",
                27.20,
                "Aucune remise",
                "m",
                "grey",
                "madishop/tshirt/tshirt_jjones_mont_grey.jpg",
            ],
            [
                "T-shirt imprimé montagne - JACK & JONES",
                "AB062",
                27.20,
                "Aucune remise",
                "l",
                "grey",
                "madishop/tshirt/tshirt_jjones_mont_grey.jpg",
            ],
            [
                "T-shirt imprimé montagne - JACK & JONES",
                "AB063",
                27.20,
                "Aucune remise",
                "xl",
                "grey",
                "madishop/tshirt/tshirt_jjones_mont_grey.jpg",
            ],
            [
                "T-shirt imprimé montagne - JACK & JONES",
                "AB064",
                25.80,
                "Aucune remise",
                "s",
                "black",
                "madishop/tshirt/tshirt_jjones_mont_black.jpg",
            ],
            [
                "T-shirt imprimé montagne - JACK & JONES",
                "AB065",
                25.80,
                "Aucune remise",
                "m",
                "black",
                "madishop/tshirt/tshirt_jjones_mont_black.jpg",
            ],
            [
                "T-shirt imprimé montagne - JACK & JONES",
                "AB066",
                25.80,
                "Aucune remise",
                "l",
                "black",
                "madishop/tshirt/tshirt_jjones_mont_black.jpg",
            ],
            [
                "T-shirt imprimé montagne - JACK & JONES",
                "AB067",
                25.80,
                "Aucune remise",
                "xl",
                "black",
                "madishop/tshirt/tshirt_jjones_mont_black.jpg",
            ],

        ]
        try:
            for item in items:
                siz = Size.objects.get(size_key=item[4])
                col = Color.objects.get(color_key=item[5])
                img = Image.objects.get(path_1=item[6])
                entry = Product.objects.create(
                    article=Article.objects.get(name=item[0]),
                    sku=item[1],
                    price=item[2],
                    discount=Discount.objects.get(name=item[3]),
                )
                entry.sizes.add(siz)
                entry.colors.add(col)
                entry.images.add(img)
            print("Les données ont bien été chargées dans la table 'Product'.")
        except KeyError:
            print("Une erreur s'est produite. Ces données sont déjà présentes dans la table 'Product'.")
