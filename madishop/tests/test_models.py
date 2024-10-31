from django.test import TestCase
from madishop.models import Category, Discount, Size, Color, Image, Article, Product, CartItem


class MadishopModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        categories = [["Fromages", "desc1"], ["Chaussures", "desc2"],]
        for cat in categories:
            Category.objects.create(name=cat[0], description=cat[1])
        discounts = [["discount1", "desc1", 60],]
        for discount in discounts:
            Discount.objects.create(name=discount[0], description=discount[1], percentage=discount[2])
        sizes = [["small", "Small Size"], ["big", "Big Size"],]
        for size in sizes:
            Size.objects.create(size_key=size[0], display=size[1])
        colors = [["blue", "Couleur Bleue"], ["red", "Couleur Rouge"],]
        for color in colors:
            Color.objects.create(color_key=color[0], display=color[1])
        images = [["folder/fake_img1.jpg"], ["folder/fake_img2.jpg"],]
        for image in images:
            Image.objects.create(path_1=image[0])
        art1 = ["art1", "desc1", "desc1_full", 0, 20, "Fromages", "folder/fake_img1.jpg"]
        art2 = ["art2", "desc2", "desc2_full", 10, 40, "Chaussures", "folder/fake_img2.jpg"]
        e1 = Article.objects.create(
            name=art1[0], desc_short=art1[1], desc_full=art1[2], weight=art1[3],
            capacity=art1[4], category=Category.objects.get(name=art1[5]))
        e1.images.add(Image.objects.get(path_1=art1[6]))
        e2 = Article.objects.create(
            name=art2[0], desc_short=art2[1], desc_full=art2[2], weight=art2[3],
            capacity=art2[4], category=Category.objects.get(name=art2[5]))
        e2.images.add(Image.objects.get(path_1=art2[6]))
        prd1 = ["art1", "0A3", 23.10, "discount1", "folder/fake_img1.jpg"]
        prd2 = ["art2", "0AA", 5.10, "discount1", "red", "big", "folder/fake_img2.jpg"]
        e1 = Product.objects.create(
            article=Article.objects.get(name=prd1[0]), sku=prd1[1], price=prd1[2],
            discount=Discount.objects.get(name=prd1[3]))
        e1.images.add(Image.objects.get(path_1=prd1[4]))
        e2 = Product.objects.create(
            article=Article.objects.get(name=prd2[0]), sku=prd2[1], price=prd2[2],
            discount=Discount.objects.get(name=prd2[3]))
        e2.images.add(Image.objects.get(path_1=prd2[6]))
        e2.colors.add(Color.objects.get(color_key=prd2[4]))
        e2.sizes.add(Size.objects.get(size_key=prd2[5]))


    def test_article_table(self):
        article1 = Article.objects.get(id=1)
        field_name_label = article1._meta.get_field('name').verbose_name
        self.assertEquals(field_name_label, "Nom du produit")