from madishop.models import CartItem
from django.shortcuts import get_list_or_404


def get_nb_in_cart():
    """ Gets number of articles in the cart """
    cart_nb = 0
    if cart_list := CartItem.objects.all():
        for cart in cart_list:
            cart_nb += cart.quantity
        return cart_nb
    return 0


def get_total_in_cart():
    """ Gets the total in CartItem """
    total = 0
    if cart_list := CartItem.objects.all():
        for item in cart_list:
            total += item.total
        return total, cart_list
    return None, None


# def create_sizes_dict(data):
#     """ Converts string into dictionnary """
    # sizes_dict = dict()
    # data_list = data.split(",")
    # for item in data_list:
    #     element = item.split(":")
    #     sizes_dict[element[0]] = element[1]
    # return sizes_dict


# def create_colors_dict(pictures, colors_list):
#     """ Creates the dict for select colors tag """
    # colors_list = colors_list.split(",")
    # colors_dict = dict()
    # path_list = [pictures.image1_path, pictures.image2_path, pictures.image3_path, pictures.image4_path]
    # for i in range(len(colors_list)):
    #     colors_dict[path_list[i]] = colors_list[i]
    # return colors_dict
