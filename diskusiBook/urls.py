from django.urls import path
from main.views import show_main
from diskusiBook.views import show_discussion, show_post, create_post, get_post_json

app_name = 'diskusiBook'

urlpatterns = [
    path('diskusi-book/<int:id>/', show_discussion, name='show_discussion'),
    path('diskusi-book/<str:title>/', show_post, name='show_post'),
    path('create_post/<int:id>', create_post, name='create_post'),
    path('get-post/<int:id>', get_post_json, name='get_post_json'),
]