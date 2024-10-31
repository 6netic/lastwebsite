from django.core.management.base import BaseCommand
from madishop.models import Image


class Command(BaseCommand):
    help = "Populates 'Madishop Image' table."

    def handle(self, *args, **options):
        # Populates 'Image' table ##############################################################################
        images = [
            ["madishop/alcool/liqueur-st-germain.jpg"],
            ["madishop/alcool/liqueur-italicus.jpg"],

            ["madishop/eliquid/ic-fraise-framboise-basilic-50.jpg"],
            ["madishop/eliquid/ic-framboise-bleue-pitaya.jpg"],

            ["madishop/tshirt/tshirt_laredoute_collections_green.jpg"],
            ["madishop/tshirt/tshirt_jjones_mont_white.jpg"],
            ["madishop/tshirt/tshirt_jjones_mont_green.jpg"],
            ["madishop/tshirt/tshirt_jjones_mont_grey.jpg"],
            ["madishop/tshirt/tshirt_jjones_mont_black.jpg"],

        ]
        try:
            for item in images:
                Image.objects.create(path_1=item[0])
            print("Les données ont bien été insérées dans la table 'Image'.")
        except KeyError:
            print("Une erreur s'est produite. Ces données sont déjà présentes dans la table 'Image'.")

