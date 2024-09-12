from django.urls import path
from .views import Home, CatList, CatDetail, FeedingListCreate, FeedingDetail, ToyDetail, ToyListCreate, AddToyToCat, RemoveToyFromCat

urlpatterns = [
  path('', Home.as_view(), name='home'),
  # new routes below 
  path('cats/', CatList.as_view(), name='cat-list'),
  path('cats/<int:id>/', CatDetail.as_view(), name='cat-detail'),
  path('cats/<int:cat_id>/feedings/', FeedingListCreate.as_view(), name='feeding-list-create'),
	path('cats/<int:cat_id>/feedings/<int:id>/', FeedingDetail.as_view(), name='feeding-detail'),
  path('cats/<int:cat_id>/toys/<int:id>/', ToyDetail.as_view(), name='toy-detail'),
  path('cats/<int:cat_id>/toys', ToyListCreate.as_view(), name='toy-list-create'),
  path('cats/<int:cat_id>/add_toy/<int:toy_id>/', AddToyToCat.as_view(), name='add-toy-to-cat'),
  path('cats/<int:cat_id>/remove_toy/<int:toy_id>/', RemoveToyFromCat.as_view(), name='remove-toy-from-cat'),
]
