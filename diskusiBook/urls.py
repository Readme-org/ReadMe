from django.urls import path
from main.views import show_main
from diskusiBook.views import show_discussion, show_post, create_post, get_post_json, remove_post, edit_post

app_name = 'diskusiBook'

urlpatterns = [
    path('diskusi-book/<int:id>/', show_discussion, name='show_discussion'),
    path('show_post/<int:id>', show_post, name='show_post'),
    path('create_post/<int:id>', create_post, name='create_post'),
    path('get_post/<int:id>', get_post_json, name='get_post_json'),
    path('remove_post/<int:id>', remove_post, name='remove_post'),
    path('edit_post/<int:id>', edit_post, name='edit_post'),
]