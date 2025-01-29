from django.urls import path
from Ice_Cream import views


urlpatterns = [
    path("new-product/",views.create_new_product,name='new_product'),
    path("update-orange/<int:product_id>",views.update_orange,name='Updating_Orange_Flavored_weights'),
    path("fetch-items/",views.fetch_all_items,name ='Fetching_all_items'),
    path("fetch-one/",views.fetch_one_item,name="Fetching_one_item"),
    path("fetch-many/",views.fetch_many_items,name="fetching_many_items"),
]
