from django.urls import path
from main.views import show_main
from ratingBook.views import show_rating

app_name = 'ratingBook'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('rating-book/<int:id>/', show_rating, name='show_rating'),
]