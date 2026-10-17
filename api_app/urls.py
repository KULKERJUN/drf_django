from django.urls import path
from api_app.views import *

urlpatterns = [
    path('products/',product_view,name='product_view'),
    path('products_detail/<int:p_id>/',product_detail_view,name='product_detail_view'),
]