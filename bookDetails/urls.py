from django.urls import path
from main.views import show_main
from bookDetails.views import show_details, show_details_myBook

app_name = 'bookDetails'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('details-book/allBook/<int:id>/', show_details, name='show_details'),
    path('details-book/myBook/<int:id>/', show_details_myBook, name='show_details_myBook'),
]