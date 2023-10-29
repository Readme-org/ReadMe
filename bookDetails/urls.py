from django.urls import path
from main.views import show_main
from bookDetails.views import show_details

app_name = 'bookDetails'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('details-book/<int:id>/', show_details, name='show_details'),
]