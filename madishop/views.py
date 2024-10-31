from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.urls import reverse
from madishop.models import Category, Discount, Size, Color, Image, Article, Product, CartItem, Order
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from madishop import utils
from django.utils.html import escape
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


User = get_user_model()


def home(request):
    """ Homepage view for madishop """
    nb_in_cart = utils.get_nb_in_cart()
    return render(request, "madishop/home.html", locals())


def list_all_prds(request):
    """ View to list all products in the database """
    nb_in_cart = utils.get_nb_in_cart()
    prds = Product.objects.all().distinct('article')
    return render(request, "madishop/list_all_prds.html", locals())


def list_prds_in_category(request, category):
    """ View to list products depending on its category """
    nb_in_cart = utils.get_nb_in_cart()
    prds = Product.objects.all().distinct('article').filter(article__category=Category.objects.get(name=category).pk)
    return render(request, "madishop/list_prds_in_category.html", locals())


def prd_detail(request, category, article_id):
    """ Detail view for a product """
    color_dict, size_dict, imgpath_dict = {}, {}, {}
    nb_in_cart = utils.get_nb_in_cart()
    prds = Product.objects.all().filter(article__pk=article_id)
    for prd in prds:
        for col in prd.colors.all():
            if col.color_key != "":
                color_dict[col.color_key] = col.display
        for siz in prd.sizes.all():
            if siz.size_key != "":
                size_dict[siz.size_key] = siz.display
        for img in prd.images.all():
            if color_dict:
                # imgpath_dict[list(color_dict.keys())[-1]] = img.path_1.url
                imgpath_dict[list(color_dict.values())[-1]] = img.path_1.url
            else:
                imgpath = img.path_1.url
    return render(request, "madishop/prd_detail.html", locals())


def add_to_cart(request):
    if request.method == "POST":
        art_id = escape(request.POST.get("art_id"))
        prd_qty = int(request.POST.get("this_qty"))
        if request.POST.get("colorSlt"):
            color = Color.objects.get(display=escape(request.POST.get("colorSlt"))).color_key
        else:
            color = ""
        if request.POST.get("sizeSlt"):
            size = escape(request.POST.get("sizeSlt"))
        else:
            size = ""
        prd = Product.objects.filter(
            article__pk=art_id).filter(sizes__size_key=size).filter(colors__color_key=color)
        qty_left_in_stock = prd[0].in_stock
        prd_in_cart = CartItem.objects.filter(product=Product.objects.get(pk=prd[0].pk))
        if prd_in_cart:
            qty_left_in_stock -= prd_in_cart[0].quantity
        if prd_qty > qty_left_in_stock:
            nb_in_cart = utils.get_nb_in_cart()
            return JsonResponse({"message": "Stock épuisé", "nb_in_cart": nb_in_cart})
        cart_item, _ = CartItem.objects.get_or_create(product=Product.objects.get(pk=prd[0].pk))
        _ = cart_item.add_or_modifQty_item(Product.objects.get(pk=prd[0].pk), prd_qty, "add")
        nb_in_cart = utils.get_nb_in_cart()
        return JsonResponse({"message": "Ajouté au Panier", "nb_in_cart": nb_in_cart})


def display_cart(request):
    """ Displays contents, modify them with AJAX and deletes article(s) from the cart """
    if request.method == "POST":
        prd_id = escape(request.POST.get("prd_id"))
        prd_qty = int(request.POST.get("this_qty"))
        cart_item = CartItem.objects.get(product=prd_id)
        total = cart_item.add_or_modifQty_item(Product.objects.get(pk=prd_id), prd_qty, "modify")
        total_set, _ = utils.get_total_in_cart()
        nb_in_cart = utils.get_nb_in_cart()
        return JsonResponse({"total": total, "total_set": total_set, "nb_in_cart": nb_in_cart})
    nb_in_cart = utils.get_nb_in_cart()
    new_total_set, cart = utils.get_total_in_cart()
    return render(request, "madishop/cart.html", locals())


def remove_item(request):
    """ Deletes an article from the cart with AJAX """
    if request.method == "POST":
        prd_id = escape(request.POST.get("prd_id"))
        cart_item = CartItem.objects.get(product=prd_id)
        cart_item.delete()
        nb_in_cart = utils.get_nb_in_cart()
        return JsonResponse({"nb_in_cart": nb_in_cart})


def signup(request):
    """ View for account creation of a customer """
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(
            first_name=first_name, last_name=last_name, user_email=email, username=username, password=password)
        login(request, user)
        return redirect("madishop:list_all_prds")
    return render(request, "madishop/signup.html", locals())


def connect(request):
    """ Logs user in """

    if request.method == "POST":
        user_email = request.POST.get("email")
        password = request.POST.get("password")
        redirection = request.POST.get("redirection")
        user = authenticate(user_email=user_email, password=password)
        if user:
            login(request, user)
            return redirect(redirection)
    redirection = request.GET.get('next')
    return render(request, "madishop/login.html", locals())


def disconnect(request):
    """ Logs user out """
    logout(request)
    return redirect("madishop:home")

@login_required(login_url="/madishop/connect/")
def checkout(request):
    """ View for payment """
    new_total_set, cart = utils.get_total_in_cart()
    return render(request, "madishop/checkout.html", locals())



# def test(request):
#     """ View only to test appearance on html pages """
#     return render(request, "madishop/test_file.html")
