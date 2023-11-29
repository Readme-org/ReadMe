from django.urls import path
from ratingBook import views

app_name = 'ratingBook'

urlpatterns = [
    path('', views.show_rating, name='show_rating'),
    path('reviews/<int:id>/', views.get_rating_json, name='get_rating'),
    path('reviews/<int:id>/update/', views.show_rating_to_update, name='show_rating_to_update'),
    path('reviews/<int:id>/delete/', views.delete_rating, name='delete_rating'),
    path('reviews/create/', views.create_rating_ajax, name='create_rating'),
    path('reviews/update/', views.update_rating_ajax, name='update_rating'),
    path('rating-json/', views.show_rating_json, name='show_rating_json'), 
]