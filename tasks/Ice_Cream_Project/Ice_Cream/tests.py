from django.test import TestCase
import pytest
from Ice_Cream.models import IceCreamInfo


@pytest.fixture
def new_product_data():
    product_details = {
        "ice_cream_flavour" : "Vanilla",
        "ice_cream_name" : "Vanilla Delight",
        "ice_cream_weight" : "200gms"
    }
    return product_details

@pytest.mark.django_db
def test_new_product(client,new_product_data):
    """Writing Testcase for adding new product to the list"""
    response = client.post('/icecream/new-product/', data=new_product_data)
    # print(response.json())
    print(response)
    res = response.json()
    assert res["ice_cream_flavour"] == "Vanilla"
    assert res["ice_cream_name"] == "Vanilla Delight"
    assert res["ice_cream_weight"] == "200gms"

@pytest.fixture
def update_product():
    product = IceCreamInfo.objects.create(
        ice_cream_flavour = "Orange",
        ice_cream_weight = "200gms",
    )
    return product.id

@pytest.mark.django_db
def test_product_data(client,update_product):
    """Writing Testcase for updating Orange Flavoured products from 200gms to 250gms"""
    update_dict = {
        "old_ice_cream_weight": "200gms",
        "new_ice_cream_weight": "250gms"
    }

    response = client.post(f'/icecream/update-orange/{update_product}',
                           data = update_dict)
    res = response.json()
    expected_output = {
        "ice_cream_flavour": "Orange",
        "old_ice_cream_weight": "200gms",
        "new_ice_cream_weight": "250gms"
    }
    assert res['ice_cream_flavour'] == expected_output['ice_cream_flavour']
    assert res['old_ice_cream_weight'] == expected_output['old_ice_cream_weight']
    assert res['new_ice_cream_weight'] == expected_output['new_ice_cream_weight']



@pytest.fixture
def create_one_item():
    item = IceCreamInfo.objects.create(ice_cream_name="Vanilla Delight",
                                       ice_cream_weight="200gms")

@pytest.mark.django_db
def test_fetch_one(client,create_one_item):
    """fetching one item from the menu"""
    dict_data ={
        "ice_cream_name": "Vanilla Delight",
        "ice_cream_weight": "200gms"
    }
    response = client.post('/icecream/fetch-one/',data=dict_data)
    res_data = response.json()
    expected_output = {
        "ice_cream_name": "Vanilla Delight",
        "ice_cream_weight": "200gms"
    }
    assert res_data['ice_cream_name'] == expected_output['ice_cream_name']
    assert res_data['ice_cream_weight'] == expected_output['ice_cream_weight']

@pytest.fixture
def create_many_items():
    item1 = IceCreamInfo.objects.create(ice_cream_flavour = "Chocolate",
                                        ice_cream_name = "Chocolate Blast",
                                        ice_cream_weight = "500gms")
    item2 = IceCreamInfo.objects.create(ice_cream_flavour="Vanilla",
                                        ice_cream_name="Vanilla Delight",
                                        ice_cream_weight="100gms")

@pytest.mark.django_db
def test_many_items(client,create_many_items):
    dict_data = {
        "flavour1":"Chocolate",
        "flavour2":"Vanilla"
    }
    response = client.post("/icecream/fetch-many/",data = dict_data)
    response_data = response.json()
    print(response_data)

    ice_cream_names = [item['ice_cream_name'] for item in response_data['customer choice']]
    print(ice_cream_names)
    ice_cream_weights = [item['ice_cream_weight'] for item in response_data['customer choice']]
    print(ice_cream_weights)
    assert "Chocolate Blast" in ice_cream_names
    assert "Vanilla Delight" in ice_cream_names
    assert "500gms" in ice_cream_weights
    assert "100gms" in ice_cream_weights