import json

from django.shortcuts import render
from Ice_Cream.models import IceCreamInfo
import random
from django.http import JsonResponse


def create_new_product(request):
    """To save new product """
    if request.method == "POST":
        data = request.POST
        ice_cream_flavour = data.get('ice_cream_flavour')
        ice_cream_name = data.get('ice_cream_name')
        ice_cream_weight = data.get('ice_cream_weight')
        new_product = IceCreamInfo.objects.create(
            ice_cream_flavour=ice_cream_flavour,
            ice_cream_name=ice_cream_name,
            ice_cream_weight=ice_cream_weight
        )
        new_product_data = {
            'ice_cream_flavour': new_product.ice_cream_flavour,
            'ice_cream_name': new_product.ice_cream_name,
            'ice_cream_weight': new_product.ice_cream_weight
        }

        return JsonResponse(new_product_data)


def update_orange(request,product_id):
    """updating Orange Flavored product's weight from 200gms to 250gms"""

    if request.method == "POST":
        data = request.POST
        ice_cream_flavour = data.get('ice_cream_flavour')
        old_ice_cream_weight = data.get('old_ice_cream_weight')
        new_ice_cream_weight = data.get('new_ice_cream_weight')
        product = IceCreamInfo.objects.get(id=product_id,ice_cream_flavour="Orange")
        old_ice_cream_weight = product.ice_cream_weight
        product.ice_cream_weight = new_ice_cream_weight
        product.save()
        updated_product_data = {
            'ice_cream_flavour': product.ice_cream_flavour,
            'old_ice_cream_weight': old_ice_cream_weight,
            'new_ice_cream_weight': new_ice_cream_weight
        }

        return JsonResponse(updated_product_data)


def fetch_all_items(request):
    """Extracting all the items from the menu"""
    fetch_data = IceCreamInfo.objects.all()
    print(fetch_data)
    product_list =[ {
        'ice_cream_flavour': item.ice_cream_flavour,
        'ice_cream_name': item.ice_cream_name,
        'ice_cream_weight': item.ice_cream_weight
    } for item in fetch_data]
    print(product_list)
    res = {"all items": product_list}
    return JsonResponse(res)

def fetch_one_item(request):
    """fetch one item from the menu"""
    if request.method == "POST":
        data = request.POST
        name = data.get('ice_cream_name')
        weight = data.get('ice_cream_weight')
        customer_choice =IceCreamInfo.objects.get(ice_cream_name=name,ice_cream_weight=weight)
        try:
            if customer_choice:
                response_data = {
                    'ice_cream_name':customer_choice.ice_cream_name,
                    'ice_cream_weight':customer_choice.ice_cream_weight
                }
                print(response_data)
                return JsonResponse(response_data)
            else:
                res = {"msg": "selected ice cream is not available"}
                return JsonResponse(res)
        except ValueError:
            print("please enter ice-cream name only")

def fetch_many_items(request):
    """fetching customer's choice ice creams from the menu"""
    if request.method == "POST":
        data = request.POST
        flavour1 = data.get('flavour1')
        flavour2 = data.get('flavour2')
        cst_choice = IceCreamInfo.objects.filter(ice_cream_flavour__in=[flavour1,flavour2])
        response_data =[ {
            "ice_cream_name": item.ice_cream_name,
            "ice_cream_weight": item.ice_cream_weight
                        } for item in cst_choice]
        res = {"customer choice":response_data}
        return JsonResponse(res)