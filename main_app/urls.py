from django.urls import path
from .views import Home, CatList, CatDetail, FeedingListCreate, FeedingDetail, ToyDetail, ToyListCreate

urlpatterns = [
  path('', Home.as_view(), name='home'),
  # new routes below 
  path('cats/', CatList.as_view(), name='cat-list'),
  path('cats/<int:id>/', CatDetail.as_view(), name='cat-detail'),
  path('cats/<int:cat_id>/feedings/', FeedingListCreate.as_view(), name='feeding-list-create'),
	path('cats/<int:cat_id>/feedings/<int:id>/', FeedingDetail.as_view(), name='feeding-detail'),
  path('cats/<int:cat_id>/toys/<int:id>/', ToyDetail.as_view(), name='toy-detail'),
  path('cats/<int:cat_id>/toys', ToyListCreate.as_view(), name='toy-list-create')
]
