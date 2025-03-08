from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Item

# A & B. Get all items or Filter items by search
def get_items(request):
    search_query = request.GET.get('search', '')
    if search_query:
        items = Item.objects.filter(name__icontains=search_query)
    else:
        items = Item.objects.all()
    data = [{"id": item.id, "name": item.name, "description": item.description, "price": item.price} for item in items]
    return JsonResponse(data, safe=False)

# C. Add new item
@csrf_exempt
def add_item(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            item = Item.objects.create(
                name=data['name'],
                description=data['description'],
                price=data['price']
            )
            return JsonResponse({"message": "Item added successfully!", "id": item.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)

# D. Get a single item
def get_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
        data = {"id": item.id, "name": item.name, "description": item.description, "price": item.price}
        return JsonResponse(data)
    except Item.DoesNotExist:
        return JsonResponse({"error": "Item not found"}, status=404)

# E. Update item
@csrf_exempt
def update_item(request, item_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            item = Item.objects.get(id=item_id)
            item.name = data.get('name', item.name)
            item.description = data.get('description', item.description)
            item.price = data.get('price', item.price)
            item.save()
            return JsonResponse({"message": "Item updated successfully!"})
        except Item.DoesNotExist:
            return JsonResponse({"error": "Item not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)

# F. Delete item
@csrf_exempt
def delete_item(request, item_id):
    if request.method == 'DELETE':
        try:
            item = Item.objects.get(id=item_id)
            item.delete()
            return JsonResponse({"message": "Item deleted successfully!"})
        except Item.DoesNotExist:
            return JsonResponse({"error": "Item not found"}, status=404)
    return JsonResponse({"error": "Invalid request"}, status=400)
