from django.urls import path
from main.views import show_main
from diskusiBook.views import show_diskusi, show_posts, show_thread, create_post

app_name = 'diskusiBook'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('diskusi-book/<int:id>/', show_diskusi, name='show_diskusi'),
    path('discussion/<slug>/', show_posts, name='show_posts'),
    path('thread/<slug>/', show_thread, name='show_thread'),
    path('create_post', create_post, name='create_post'),
]