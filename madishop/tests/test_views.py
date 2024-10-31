from django.test import TestCase
from madishop.models import Category, Discount, Size, Color, Image, Article, Product, CartItem
from django.urls import reverse
from decimal import Decimal


class MadishopViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        ########################     Category     ###############################################################
        categories = [["Fromages", "desc1"], ["Chaussures", "desc2"],]
        for cat in categories:
            Category.objects.create(name=cat[0], description=cat[1])
        ########################     Discount     ###############################################################
        discounts = [["discount1", "desc1", 60],]
        for discount in discounts:
            Discount.objects.create(name=discount[0], description=discount[1], percentage=discount[2])
        ########################     Size     ###################################################################
        sizes = [["small", "Small Size"], ["big", "Big Size"], ["", ""]]
        for size in sizes:
            Size.objects.create(size_key=size[0], display=size[1])
        ########################     Color     ##################################################################
        colors = [["blue", "Couleur Bleue"], ["red", "Couleur Rouge"], ["", ""]]
        for color in colors:
            Color.objects.create(color_key=color[0], display=color[1])
        ########################     Image     ##################################################################
        images = [["folder/fake_img1.jpg"], ["folder/fake_img2.jpg"],]
        for image in images:
            Image.objects.create(path_1=image[0])
        ########################     Article     ################################################################
        articles = [
            ["art1", "descArt1", "desc1_full", 0, 20, "Fromages", "folder/fake_img1.jpg"],
            ["art2", "descArt2", "desc1_full", 12, 43, "Chaussures", "folder/fake_img2.jpg"],
            ["art3", "descArt3", "desc1_full", 0, 20, "Chaussures", "folder/fake_img2.jpg"],
        ]
        for art in articles:
            entry = Article.objects.create(
                name=art[0], desc_short=art[1], desc_full=art[2], weight=art[3],
                capacity=art[4], category=Category.objects.get(name=art[5]))
            entry.images.add(Image.objects.get(path_1=art[6]))
        ########################     Product     ###############################################################
        products = [
            ["art1", "0A3", 23.10, "discount1", "folder/fake_img1.jpg", "", "", 2],
            ["art2", "96", 9.80, "discount1", "folder/fake_img2.jpg", "blue", "small", 2],
            ["art3", "0AA", 5.10, "discount1", "folder/fake_img2.jpg", "red", "big", 2]
        ]
        for prd in products:
            entry = Product.objects.create(
                article=Article.objects.get(name=prd[0]), sku=prd[1], price=prd[2],
                discount=Discount.objects.get(name=prd[3]), in_stock=prd[7])
            entry.images.add(Image.objects.get(path_1=prd[4]))
            entry.colors.add(Color.objects.get(color_key=prd[5]))
            entry.sizes.add(Size.objects.get(size_key=prd[6]))
        ########################     CartItem     ###############################################################
        CartItem.objects.create(product=Product.objects.get(pk=2), quantity=1, total=26.20)


    def test_home_view(self):
        """ - Tester la page d'accueil """
        # art_nb = Article.objects.all().count()
        response = self.client.get(reverse("madishop:home"))
        # self.assertEquals(art_nb, len(response.context['prds']))
        self.assertEquals(response.context['nb_in_cart'], 1)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "madishop/home.html")

    def test_list_all_prds(self):
        """ - Tester que l'on a tous les produits de la database """
        response = self.client.get(reverse("madishop:list_all_prds"))
        self.assertEquals(response.context['nb_in_cart'], 1)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "madishop/list_all_prds.html")
        self.assertEquals(len(response.context['prds']), 3)

    def test_list_prds_in_category(self):
        """ - Tester le bon nb de produits dans une catégorie """
        response = self.client.get(reverse("madishop:list_prds_in_category", kwargs={"category": "Chaussures"}))
        self.assertEquals(len(response.context['prds']), 2)
        self.assertEquals(response.context['nb_in_cart'], 1)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "madishop/list_prds_in_category.html")

    def test_prd_detail(self):
        """ - Tester le détail d'un produit """
        # tester aucun article trouvé
        response = self.client.get(reverse("madishop:prd_detail",
                    kwargs={"category": "Chaussures", "article_id": Article.objects.get(name="art3").pk}))
        self.assertEquals(len(response.context['prds']), 1)
        self.assertEquals(response.context['prds'][0].get_color(), "red")
        self.assertEquals(response.context['prds'][0].get_size(), "big")
        self.assertEquals(response.context['prds'][0].get_image(), "folder/fake_img2.jpg")
        response = self.client.get(reverse("madishop:prd_detail",
                    kwargs={"category": "Fromages", "article_id": Article.objects.get(name="art1").pk}))
        self.assertEquals(response.context['prds'][0].get_color(), "")
        self.assertEquals(response.context['prds'][0].get_size(), "")
        self.assertEquals(response.context['imgpath'], "/media/" + response.context['prds'][0].get_image())
        self.assertEquals(response.context['nb_in_cart'], 1)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "madishop/prd_detail.html")


    def test_add_to_cart(self):
        # no size, no color, prd not in cart yet
        response = self.client.post(reverse("madishop:add_to_cart"), {
                    "art_id": Article.objects.get(pk=1).pk, "this_qty": 1})
        self.assertEquals(CartItem.objects.all().count(), 2)
        self.assertEquals(response.json()['nb_in_cart'], 2)
        # no size, no color, prd already in cart
        response = self.client.post(reverse("madishop:add_to_cart"), {
            "art_id": Article.objects.get(pk=1).pk, "this_qty": 1})
        self.assertEquals(CartItem.objects.all().count(), 2)
        self.assertEquals(response.json()['nb_in_cart'], 3)
        self.assertEquals(response.json()['message'], "Ajouté au Panier")
        # no size, no color, nb of prds exceeds qty in stock
        response = self.client.post(reverse("madishop:add_to_cart"), {
            "art_id": Article.objects.get(pk=1).pk, "this_qty": 2})
        self.assertEquals(CartItem.objects.all().count(), 2)
        self.assertEquals(response.json()['nb_in_cart'], 3)
        self.assertEquals(response.json()['message'], "Stock épuisé")
        # size and color given, prd not in cart yet
        response = self.client.post(reverse("madishop:add_to_cart"), {
                "art_id": Article.objects.get(pk=3).pk, "this_qty": 2, "colorSlt": "Couleur Rouge", "sizeSlt": "big"})
        self.assertEquals(CartItem.objects.all().count(), 3)
        self.assertEquals(response.json()['nb_in_cart'], 5)
        self.assertEquals(response.json()['message'], "Ajouté au Panier")
        # size and color given, nb of prds exceeds qty in stock
        response = self.client.post(reverse("madishop:add_to_cart"), {
            "art_id": Article.objects.get(pk=3).pk, "this_qty": 1, "colorSlt": "Couleur Rouge", "sizeSlt": "big"})
        self.assertEquals(CartItem.objects.all().count(), 3)
        self.assertEquals(response.json()['nb_in_cart'], 5)
        self.assertEquals(response.json()['message'], "Stock épuisé")


    def test_display_cart(self):
        """ - Tests display cart view """
        # get method
        response = self.client.get(reverse("madishop:display_cart"))
        self.assertEquals(response.context['nb_in_cart'], 1)
        self.assertEquals(response.context['new_total_set'], Decimal('26.20'))
        self.assertEquals(CartItem.objects.all().count(), 1)
        # post method
        response = self.client.post(reverse("madishop:add_to_cart"), {
            "art_id": Article.objects.get(pk=3).pk, "this_qty": 2, "colorSlt": "Couleur Rouge", "sizeSlt": "big"})
        self.assertEquals(CartItem.objects.all().count(), 2)
        self.assertEquals(response.json()['nb_in_cart'], 3)
        response = self.client.post(reverse("madishop:display_cart"), {
            "prd_id": Product.objects.get(pk=3).pk, "this_qty": 1})
        self.assertEquals(response.json()['nb_in_cart'], 2)
        self.assertEquals(response.json()['total'], "5.10")
        self.assertEquals(response.json()['total_set'], "31.30")


    def test_remove_item(self):
        """ - Tests remove item view """
        response = self.client.post(reverse("madishop:remove_item"), {"prd_id": Product.objects.get(pk=2).pk})
        self.assertEquals(response.json()['nb_in_cart'], 0)




