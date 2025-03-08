from django.urls import path
from . import views

urlpatterns = [
    path('api/items/', views.get_items, name='get_items'),  # a. Get all items, b. Filter items
    path('api/items/add/', views.add_item, name='add_item'),  # c. Add new item
    path('api/items/<int:item_id>/', views.get_item, name='get_item'),  # d. Get single item
    path('api/items/update/<int:item_id>/', views.update_item, name='update_item'),  # e. Update item
    path('api/items/delete/<int:item_id>/', views.delete_item, name='delete_item'),  # f. Delete item
]
