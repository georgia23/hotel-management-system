from django.shortcuts import redirect, render

from .models import Category, Room
from .forms import RoomForm , CategoryForm

# Create your views here.


def roomsList(request):
    all_rooms = Room.objects.all()

    context = {
        'rooms_list': all_rooms
    }

    return render(request, 'index.html', context)


def rooms(request):

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('roomsList')
        
    else:
        form = RoomForm()

    return render(request, 'rooms.html', {'form': form})


def editRoom(request, room_id):

    room = Room.objects.get(id=room_id)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('roomsList')
        
    else:
        form = RoomForm(instance=room)

    return render(request, 'rooms.html', {'form': form})

def category(request):

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoryList')
        
    else:
        form = CategoryForm()

    return render(request, 'category.html', {'form': form})

def categoryList(request):
    all_categories = Category.objects.all()

    context = {
        'categories': all_categories
    }


    return render(request, 'categoryList.html', context)


def editCategory(request, category_id):

    category = Category.objects.get(id=category_id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categoryList')
        
    else:
        form = CategoryForm(instance=category)

    return render(request, 'category.html', {'form': form})

def base(request):

    return render(request, 'base.html')
