from django.urls import path
from main.views import show_main
from diskusiBook.views import show_diskusi

app_name = 'diskusiBook'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('diskusi-book/<int:id>/', show_diskusi, name='show_diskusi'),
]