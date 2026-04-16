from django.urls import path
from .views import rooms, roomsList, base, category, categoryList, editRoom, editCategory

urlpatterns = [
    
    path('', roomsList, name="roomsList"),
    path('rooms', rooms , name="rooms"),
    path('rooms/<int:room_id>/edit', editRoom, name="editRoom"),
    path('categoryList', categoryList, name="categoryList"),
    path('category', category , name="category"),
    path('categoryList/<int:category_id>/edit', editCategory, name="editCategory"),
    path('base', base, name="base")
]
