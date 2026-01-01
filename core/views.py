
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})
def create_item(request):
    form = ItemForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return render(request, 'partials/item_list.html', {
            'items': Item.objects.all()
        })
    return render(request, 'partials/item_form.html', {'form': form})

def update_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    form = ItemForm(request.POST or None, instance=item)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return render(request, 'partials/item_list.html', {'items': Item.objects.all()})
    return render(request, 'partials/item_form.html', {'form': form, 'item': item})

def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return render(request, 'partials/item_list.html', {'items': Item.objects.all()})
    return render(request, 'partials/confirm_delete.html', {'item': item})
