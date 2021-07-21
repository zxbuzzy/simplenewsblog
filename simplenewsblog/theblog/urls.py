from django.urls import path
# from . import views
from .views import HomeView, ArticleDetatilView, AddPostView

urlpatterns = [
    # path('', views.home, name="home")
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetatilView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
]
