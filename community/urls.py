from django.urls import path
from main.views import show_main
from community.views import show_community

app_name = 'community'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('community/<int:id>/', show_community, name='show_community'),
]