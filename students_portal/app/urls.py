from django.urls import path
from . import views
app_name = 'app'

urlpatterns = [
    path('',views.posts_list,name = "list"),
    path('<slug:slug>',views.posts_page,name = "page"),
]