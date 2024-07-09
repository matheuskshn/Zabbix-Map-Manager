from django.urls import path
from . import views

urlpatterns = [
    path('create-map/', views.create_map_view, name='create_map_view'),
    path('map-result/', views.map_result_view, name='map_result'),
    # ... outras URLs
]
