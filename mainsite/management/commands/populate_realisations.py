from django.core.management.base import BaseCommand
from mainsite.models import Realisation


class Command(BaseCommand):
    """ Populates Mainsite table """

    help = "Populates Mainsite table."

    def handle(self, *args, **options):
        """ Liste des realisations a ce jour """

        nurse_list = [
            [
                "ATP Ranking",
                "Appli de scrapping pour récupérer le classement et les matches des joueurs de tennis "
                "de façon à pouvoir être utilisés pour des projets de machine learning.",
                "Application",
                "../../tennis_players"
            ],
            [
                "GrandPy",
                "Petit bot qui affiche la carte du lieu recherché ainsi qu'un court extrait de son histoire. "
                "Les informations sont tirées du site mediaWiki.",
                "Django",
                "../../grandpy/"
            ],
            [
                "Hunting Quizz",
                "Quizz permettant de s'entraîner pour le passage à l'examen du permis de chasse. "
                "2 modes sont proposés : normal (conditions réelles) et "
                "assisté (solution détaillée affichée pour chaque réponse donnée).",
                "Django",
                "../../hunting_quizz/"
            ],
            [
                "L'Orchidée",
                "Appli web pour un cabinet d'infirmières libérales permettant d'afficher les tournées sur une "
                "interface web plutôt que de les imprimer à partir de l'application Simply Vitale.",
                "Django",
                "../../l_orchidee/"
            ],
            [
                "Limo Réservations",
                "Interface de réservations de courses pour les clients d'un hotel vers la destination désirée.",
                "Django",
                "../../limobooking/"
            ],
            [
                "PurBeurre",
                "Site permettant de trouver un produit alimentaire plus sain que celui que vous lui proposez. "
                "Les données sont extraites d'OpenFoodFacts.",
                "Django",
                "../../purbeurre/"
            ],
            [
                "Scrape4Fun",
                "Scrapping du site books.toscrape.com.",
                "Application",
                "../../scrapping/"
            ],
            [
                "Ciblerie",
                "Interface permettant de comptabiliser les points sur une cible 10 mètres",
                "Django",
                "../../ciblerie/"
            ],
            [
                "MadiShop",
                "Exemple de site E-commerce en ligne.",
                "Django",
                "../../madishop/"
            ],
        ]
        try:
            for line in nurse_list:
                Realisation.objects.create(
                    name=line[0],
                    description=line[1],
                    techno=line[2],
                    url=line[3]
                )
            print("Les données ont bien été chargées dans la table 'Realisations'.")
        except KeyError:
            print("Une erreur s'est produite. Ces données sont déjà présentes dans la table 'Realisations'.")

