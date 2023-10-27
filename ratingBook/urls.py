from django.urls import path
from ratingBook.views import show_rating, debug

app_name = 'ratingBook'

urlpatterns = [
    path('<int:id>/', show_rating, name='show_rating'),
    path('debug/', debug, name='debug')
]