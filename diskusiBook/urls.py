from django.urls import path
from main.views import show_main
# from diskusiBook.views import show_discussion, show_post, create_post

app_name = 'diskusiBook'

urlpatterns = [
    path('', show_main, name='show_main'),
    # path('diskusi-book/<int:id>/', show_discussion, name='show_discussion'),
    # path('diskusi-book/<int:id>/<str:title>/', show_post, name='show_post'),
    # path('create_post', create_post, name='create_post'),
]