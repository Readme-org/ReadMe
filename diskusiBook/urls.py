from django.urls import path
from main.views import show_main
from diskusiBook.views import show_discussion, show_post, create_post, get_post_json, remove_post, edit_post, show_json, create_post_flutter, edit_post_flutter, remove_post_flutter, get_username, get_comment_json, get_reply_json, create_comment, edit_comment, remove_comment, get_single_post_json, create_reply, edit_reply, remove_reply, show_json_comment, show_json_reply, create_comment_flutter, edit_comment_flutter, remove_comment_flutter, create_reply_flutter, edit_reply_flutter, remove_reply_flutter

app_name = 'diskusiBook'

urlpatterns = [
    path('diskusi-book/<int:id>/', show_discussion, name='show_discussion'),
    path('show_post/<int:id>/', show_post, name='show_post'),
    path('create_post/<int:id>/', create_post, name='create_post'),
    path('get_post/<int:id>/', get_post_json, name='get_post_json'),
    path('get_single_post_json/<int:id>/', get_single_post_json, name='get_single_post_json'),
    path('get_comment/<int:id>/', get_comment_json, name='get_comment_json'),
    path('get_reply/<int:id>/', get_reply_json, name='get_reply_json'),
    path('remove_post/<int:id>/', remove_post, name='remove_post'),
    path('edit_post/<int:id>/', edit_post, name='edit_post'),
    path('create_comment/<int:id>/', create_comment, name='create_comment'),
    path('create_comment_flutter/', create_comment_flutter, name='create_comment_flutter'),
    path('remove_comment/<int:id>/', remove_comment, name='remove_comment'),
    path('remove_comment_flutter/', remove_comment_flutter, name='remove_comment_flutter'),
    path('edit_comment/<int:id>/', edit_comment, name='edit_comment'),
    path('edit_comment_flutter/', edit_comment_flutter, name='edit_comment_flutter'),
    path('create_reply/<int:id>/', create_reply, name='create_reply'),
    path('create_reply_flutter/', create_reply_flutter, name='create_reply_flutter'),
    path('remove_reply/<int:id>/', remove_reply, name='remove_reply'),
    path('remove_reply_flutter/', remove_reply_flutter, name='remove_reply_flutter'),
    path('edit_reply/<int:id>/', edit_reply, name='edit_reply'),
    path('edit_reply_flutter/', edit_reply_flutter, name='edit_reply_flutter'),
    path('json/', show_json, name='show_json'),
    path('json-comment/', show_json_comment, name='show_json_comment'),
    path('json-reply/', show_json_reply, name='show_json_reply'),
    path('create_post_flutter/', create_post_flutter, name='create_post_flutter'),
    path('edit_post_flutter/', edit_post_flutter, name='edit_post_flutter'),
    path('remove_post_flutter/', remove_post_flutter, name='remove_post_flutter'),
    path('get_username/<int:user_id>/', get_username, name='get_username'),
]